#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cv2
import matplotlib.pyplot as plt
import numpy as np

def test_similarity(img1, img2):
    ch_names = {0: "Hue", 1: "Saturation",2: "Brightness"}
    hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

    scores, hists1, hists2 = [], [], []
    for ch in ch_names:
        h1 = cv2.calcHist(
            [hsv1], [ch], None, histSize=[256], ranges=[0,256])
        h2 = cv2.calcHist(
            [hsv2], [ch], None, histSize=[256], ranges=[0,256])
        score = cv2.compareHist(h1, h2, cv2.HISTCMP_CORREL)
        hists1.append(h1)
        hists2.append(h2)
        scores.append(score)
    mean = np.mean(scores)

    fig, axes = plt.subplots(2, 2, figsize=(8, 8))
    for [axL, axR], hist, img in zip(axes, [hists1, hists2], [img1, img2]):

        axL.imshow(img[..., ::-1])
        axL.axis("off")
        for i in range(3):
            axR.plot(hist[i], label=ch_names[i])
        axR.legend()
    fig.suptitle("similarity={:.2f}".format(mean))
    plt.show()

if __name__ == "__main__":
    image1 = cv2.imread("images/gray1.png")
    image2 = cv2.imread("images/gray2.png")
    test_similarity(image1, image2)
