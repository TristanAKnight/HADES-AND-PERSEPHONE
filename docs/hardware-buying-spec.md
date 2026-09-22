# Hardware Buying Spec

Status: starter recommendation
Date: 2026-08-19

## Purpose

Define what Katerina should buy for the continuity shelter, local AI testing, Obsidian, n8n, Docker, MCP workflows, document generation, and long-session project work.

This file is a buying target, not a final shopping cart. Exact models and prices should be checked near purchase time because GPU pricing and laptop configs change fast.

## Direct recommendation

Buy a serious Windows workstation laptop only if portability matters. Buy a desktop workstation if the priority is local model power, thermal stability, upgradeability, and long work sessions.

Best practical target for Katerina:

- primary machine: high-end Windows workstation laptop with RTX 5090 Laptop GPU, 64 GB RAM, 4 TB SSD, strong cooling, and a high-quality 16-18 inch display;
- optional later machine: desktop workstation with RTX 5090 32 GB VRAM, 64-128 GB RAM, 4 TB+ SSD, and room to upgrade.

## Minimum viable local-test machine

This is the floor for running the continuity shelter locally without making every tool slow.

- OS: Windows 11 Pro or Linux-capable Windows laptop.
- CPU: current high-end Ryzen AI 9 / Core Ultra 9 class CPU.
- RAM: 64 GB.
- GPU: NVIDIA RTX 4080/5080 class or better.
- VRAM: 16 GB minimum.
- Storage: 2 TB SSD minimum.
- Docker: must run Docker Desktop or native Linux containers cleanly.

## Preferred machine

This is the right target if quality matters more than price.

- OS: Windows 11 Pro.
- CPU: high-end Ryzen AI 9 HX / Intel Core Ultra 9 HX class.
- RAM: 64 GB minimum; 96-128 GB preferred if configurable.
- GPU: RTX 5090 Laptop GPU for laptop, RTX 5090 desktop GPU for tower.
- VRAM: 24 GB minimum for a laptop RTX 5090; 32 GB for desktop RTX 5090.
- Storage: 4 TB SSD preferred; second drive slot strongly preferred.
- Display: 16-18 inch OLED/Mini-LED preferred.
- Cooling: desktop replacement chassis preferred over thin ultralight if the same GPU tier is offered.
- Ports: USB-C/Thunderbolt, HDMI/DisplayPort, enough USB-A for peripherals, Ethernet preferred.

## Best-fit laptop category

Look for a creator/workstation or desktop-replacement gaming laptop with:

- RTX 5090 Laptop GPU,
- 64 GB RAM,
- 4 TB SSD,
- strong cooling,
- non-soldered or already-maxed memory if possible,
- reliable service/warranty.

Candidate families to inspect when buying:

- ASUS ProArt P16 RTX 5090 / 64 GB / 4 TB class.
- MSI Titan 18 HX AI RTX 5090 / 64 GB / 4 TB class.
- ASUS ROG Strix Scar 18 RTX 5090 / 64 GB / 4 TB class.
- Razer Blade 16 RTX 5090 / 64 GB class if portability and build quality matter more than cooling headroom.
- Lenovo Legion Pro 7i RTX 5090 / 64 GB class if pricing is substantially better.

## Best-fit desktop category

A desktop is better if Katerina is comfortable keeping the AI shelter mostly at home.

Target:

- RTX 5090 desktop GPU with 32 GB VRAM.
- 64 GB RAM minimum; 128 GB preferred.
- 4 TB NVMe SSD minimum.
- 1000 W+ quality PSU.
- strong airflow case.
- practical warranty/support.

Avoid overpaying for bare RTX 5090 cards if prebuilt systems with the same GPU are cheaper than the card alone.

## What not to buy

- 16 GB RAM machines.
- 32 GB RAM machines unless they are clearly upgradeable.
- Integrated-GPU-only AI laptops.
- Thin laptops that throttle heavily under sustained GPU load.
- Machines with 1 TB storage only.
- Any machine where RAM is soldered at 32 GB and cannot be upgraded.
- Anything bought only because it says “AI” in the product name.

## Buying decision

If Katerina needs one machine soon and wants quality first: buy a 64 GB / 4 TB / RTX 5090 laptop in the creator or desktop-replacement class.

If Katerina can tolerate a two-machine strategy: buy a strong but comfortable daily laptop, then buy or build a desktop RTX 5090 workstation for local model work.

## Open questions before final cart

- Does Katerina need this machine to be portable every day?
- Does it need to sit comfortably in bed/lap, or can it be a heavy desktop replacement?
- Does Katerina want one machine only, or laptop plus later desktop?
- Preferred screen size: 16, 17, or 18 inches?
- Storage preference: 4 TB internal only, or 2 TB internal plus external SSD acceptable?
- Will hosted APIs remain acceptable, or should the machine be designed for maximum local inference?
