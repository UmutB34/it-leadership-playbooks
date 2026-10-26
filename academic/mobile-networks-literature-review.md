# Mobile networks and LTE: a literature review

*Graduate course project (MSc, Computer Engineering, computer architectures and networks, autumn 2022; report January 2023). Group of three; I was the group spokesperson. A literature review, not field engineering.*

## Goal

Understand how LTE networks work and where performance is won or lost, by reading and comparing six academic papers and putting them in the context of mobile network generations.

## Papers reviewed (topics and findings)

| Topic | What the paper showed |
|---|---|
| Real-time, high-resolution video over LTE | In simulation, 720p, 1080p and 2160p video was served well with few users; as users grew, proportional-fair scheduling raised delay and round-robin raised packet delay because it gives equal resources regardless of channel quality |
| Resource allocation in multi-cell LTE-Advanced with fractional frequency reuse | Cells are split into centre and edge zones; schedulers compared: proportional fair (fairness and spectral efficiency), round robin (equal share), best channel quality indicator (highest speed for users nearest the tower, no fairness), generalized proportional fair and arithmetic-mean methods |
| Power management of femto cells in heterogeneous LTE | A genetic optimization lowered femto-cell transmit power by more than half against the standard approach, cutting interference with little loss of service for users |
| Three-band, four-element MIMO antenna array for LTE and 5G terminals | A compact log-periodic patch design simulated at 2.6, 3.6 and 5.5 GHz, with coupling and isolation measured, suited to sub-6 GHz applications |
| Antenna design for a 4G base station | Design choices for base-station antennas and their effect on coverage |
| Queue management between a remote host and the packet gateway | Comparison of queue management algorithms and their performance in an LTE core |

## Background covered

- Generations: analogue voice (1G), digital voice and SMS (2G), data and video (3G), all-IP broadband (4G/LTE), very high speed and low delay (5G).
- Cells: dense cities need many small cells; rural areas use few large ones; indoor cells serve crowded buildings.
- MIMO and antenna design, and frequency reuse planning so neighbouring cells do not interfere.

## What I took from it

- **Fairness versus efficiency.** Every scheduler trades equal treatment against total throughput. The same trade-off appears in Wi-Fi sizing, bandwidth management and queue policy.
- **Capacity versus coverage.** Dense areas need more, lower-power access points; open areas need fewer.
- **Simulations need their limits stated.** A result from a simulator tells you how an algorithm behaves, not how a live network will.
- **Presenting.** As spokesperson I turned six technical papers into a short briefing for the class.

## Limits

This was an academic review. It did not involve operating a mobile network, and I do not present it as telecom delivery experience.
