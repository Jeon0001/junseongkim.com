---
title: "Detection of Stationary Atmospheric Waves in Venus with a Self-Supervised Adversarial Model Using Anomaly Detection"
collection: publications
permalink: /publication/anomaly-detection-stationary-waves
excerpt: 'Proposal for an anomaly detection scheme for identifying stationary waves in Venus' atmosphere using a self-supervised model.'
date: 2026-07-04
venue: 'Conference: 한국정보과학회 Korea Computer Conference'
paperurl: 'https://scholar.google.com/scholar?oi=bibs&cluster=17754080156825375173&btnI=1&hl=en'
citation: '//'
---

Abstract
------

In this paper, we propose an anomaly detection scheme for identifying stationary waves in Venus' atmosphere using a self-supervised model. Initially, we stack multiple images of projected maps of Venus to filter out other types of features, highlighting stationary waves. We split each image into 72✕ 72-resolution patches and designated patches with waves as anomalies. In contrast, the rest of the grids are defined as normal data. We create a variational autoencoder-based, adversarially trained anomaly detection model. We train the model using a portion of the normal data and test it with the remaining normal and anomaly data. The results show that the model can differentiate between stationary waves and cloud formations, with an AUC score of 78.37%.

[Download paper here](https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE11488198)