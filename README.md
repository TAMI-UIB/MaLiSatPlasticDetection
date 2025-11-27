# PRISMA Marine Litter Detection Analysis

This repository documents the evaluation of PRISMA hyperspectral imagery for the detection of floating marine litter.

## Overview

The goal of this work was to investigate whether PRISMA’s hyperspectral sensor could support the creation of a high-quality dataset for marine litter detection, with a focus on identifying floating plastic patches. To this end, multiple coordinated acquisitions were planned across Mediterranean locations together with known persistent plastic aggregation, and manual annotations were generated to provide pixel-level labels.

Despite these efforts, the analysis showed that PRISMA’s spatial resolution is insufficient for reliable detection, and that the hyperspectral signatures extracted for floating plastics did not yield stable or distinctive patterns under real-world conditions. These findings motivated a shift toward Sentinel-2–based datasets for subsequent model development.

## Dataset Acquisition and Manual Labeling

To evaluate PRISMA for marine litter detection:

* Satellite overpasses were scheduled over targeted Mediterranean coastal regions with documented plastic accumulation.

* Local teams collected contextual information when possible (weather, sea state, nearby sources of runoff).

* Floating plastic patches were manually annotated on PRISMA Level-2 RGB composites.

* Pixel-level masks were created marking regions with visually identifiable floating debris.

* Below is an example of an annotated scene:

PRISMA RGB Image	Plastic Mask

	
## Spectral Analysis

For each annotated scene, hyperspectral signatures were extracted from:

1. Pixels labeled as floating plastic

2. Pixels labeled as open water

The objective was to evaluate whether spectral separability existed between both classes, particularly in wavelengths where plastic is expected to have characteristic reflectance behavior.

Plastic vs. Water Reflectance

Although subtle differences were detected, they were not consistent across scenes, mainly due to:

* Sub-pixel mixing with water

* Wave glint and illumination variability

* Very small target size relative to PRISMA’s pixel footprint

As a result, no robust or reproducible spectral pattern could be identified.

## Spatial Resolution Constraints

PRISMA’s spatial resolution (30 m for hyperspectral bands) imposes a fundamental limitation:

* Most floating litter patches observed in situ are significantly smaller than a single pixel.

* Even larger accumulations tend to be thin, fragmented, and partially submerged.

* Fusion experiments (HS → PAN) were unable to produce usable detail, since the underlying signal was already too mixed at native resolution.

These issues reduce the number of usable scenes to a fraction of the total acquisitions, making large-scale dataset construction infeasible.

## Conclusions

Based on the experiments performed:

* Manual dataset construction using PRISMA is not viable for marine litter detection due to spatial resolution constraints.

* Spectral signatures of floating plastics could not be reliably extracted, even with coordinated acquisitions and manual annotations.

* Fusion techniques did not yield sufficient improvement to enable detection.

The project therefore transitioned to publicly available Sentinel-2 datasets, which provide:

* Higher spatial resolution (10 m)

* Short revisit times

* Open access

* Bands already validated in the literature for floating debris detection (e.g., spectral ranges used in FDI and NDVI)


