---
title: "Detection of Stationary Atmospheric Waves in Venus with a Self-Supervised Adversarial Model Using Anomaly Detection"
collection: publications
permalink: /publication/anomaly-detection-stationary-waves
excerpt: 'Proposal for an anomaly detection scheme for identifying stationary waves in Venus atmosphere using a self-supervised model.'
date: 2023-06-01
venue: 'Korea Computer Conference (KCC)'
paperurl: 'https://jeon0001.github.io/junseongkim.com/files/VenusPaper1.pdf'
# citation: 'Your Name, You. (2009). &quot;Paper Title Number 1.&quot; <i>Journal 1</i>. 1(1).'
---
Abstract
------

In this paper, we propose an anomaly detection scheme for identifying stationary waves in Venus' atmosphere using a self-supervised model. Initially, we stack multiple images of projected maps of Venus to filter out other types of features, highlighting stationary waves. We split each image into 72✕ 72-resolution patches and designated patches with waves as anomalies. In contrast, the rest of the grids are defined as normal data. We create a variational autoencoder-based, adversarially trained anomaly detection model. We train the model using a portion of the normal data and test it with the remaining normal and anomaly data. The results show that the model can differentiate between stationary waves and cloud formations, with an AUC score of 78.37%.

[Download paper here](https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE11488198)

or

[Download paper here](https://jeon0001.github.io/junseongkim.com/files/VenusPaper1.pdf)