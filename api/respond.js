export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const auth = req.headers.authorization;
  const proxySecret = process.env.PROXY_SECRET;
  const openaiKey = process.env.OPENAI_API_KEY;

  if (!proxySecret || !openaiKey) {
    return res.status(500).json({ error: 'Server configuration incomplete' });
  }

  if (auth !== `Bearer ${proxySecret}`) {
    return res.status(401).json({ error: 'Unauthorized' });
  }

  const body = req.body && typeof req.body === 'object' ? req.body : null;
  if (!body) {
    return res.status(400).json({ error: 'Expected JSON body' });
  }

  const allowedModels = new Set([
    'gpt-5.6',
    'gpt-5.6-mini',
    'gpt-5.6-nano'
  ]);

  if (!body.model || !allowedModels.has(body.model)) {
    return res.status(400).json({ error: 'Model is not allowlisted' });
  }

  const upstream = await fetch('https://api.openai.com/v1/responses', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${openaiKey}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
  });

  res.statusCode = upstream.status;
  const contentType = upstream.headers.get('content-type');
  if (contentType) res.setHeader('Content-Type', contentType);
  const requestId = upstream.headers.get('x-request-id');
  if (requestId) res.setHeader('x-openai-request-id', requestId);

  if (!upstream.body) {
    const text = await upstream.text();
    return res.end(text);
  }

  const reader = upstream.body.getReader();
  try {
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      res.write(Buffer.from(value));
    }
    res.end();
  } catch (error) {
    console.error('Proxy stream error', error);
    if (!res.headersSent) {
      res.statusCode = 502;
      res.setHeader('Content-Type', 'application/json');
    }
    res.end(JSON.stringify({ error: 'Upstream stream failed' }));
  }
}
