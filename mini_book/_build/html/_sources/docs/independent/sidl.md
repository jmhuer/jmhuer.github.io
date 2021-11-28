---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Shift-Invariant Dictionary Learning using Temporal CONV-WTA Autoencoders for Discovering Music Relations

 <sub> <a href="https://jmhuer.github.io/mini_book/_build/html/docs/portfolio.html" style="color: red; text-decoration: underline;text-decoration-style: dotted;">← Back to Porfolio</a> </sub>

<img src="../../../../images/sidl.png" align="center"/>

<br>

The temporal structure of music is full of shift-invariant patterns (e.g. motifs, ostinatos, loops, etc.). We propose using a Tempo- ral Convolutional Winner-Take-All (CONV- WTA) autoencoder to find a shift-invariant dictionary to represent symbolic, multivariate, musical signals. The model learns to represent fixed length drum beats and variable length pi- ano music. We discuss applications of this sparse representation such as de-noising musi- cal ideas, unsupervised learning of composer styles, and music generation. To assist in re- lated work we include interactive code along with the trained models

<br>


## Introduction
---

The dictionary learning framework aims at finding a sparse representation of the input data (sparse coding) in the form of a linear combination of ba- sic elements called atoms. In doing so, sparse coding enables faster inference and easier inter- pretability thanks to its lightweight stored mem- ory, encoding of prior knowledge in the sparsity patterns, and discerning patterns in an informed and principled manner.
Sparse dictionary learning has led to state-of-art results in various tasks including image and video processing, texture synthesis (Peyre ́, 2009), and unsupervised clustering (Ram ́ırez et al., 2010). In evaluations with the Bag-of-Words model (Ko- niusz et al., 2017), sparse coding was found empir- ically to outperform other coding approaches on category recognition tasks.
When applied to music, the ability to distil complex data structures down to sets of dictio- naries—salient features of a specific performer or music, has a multitude of applications. Music transcription and classification tasks have seen a strong usage of sparse dictionary learning in the past (Grosse et al., 2007) (Costantini et al., 2013), (Blumensath and Davies, 2006), (Srinivas M et al., 2014), (Srinivas et al., 2014), (Cogliati et al., 2016). Nonetheless, we have yet to see a study that harnesses the advantages of sparse representa- tion for the purpose of music creation. Instead, the popular methods for discovering music relations and achieving music generation have been a trans- former with some sort of attention mechanism or other recurrent architectures. For instance, (Jiang Junyan et al., 2020) uses an attention module that is tailored to the discovery of sequence level rela- tions in music, while studies like (Roberts et al., 2018) uses the recurrent variational autoencoder and a hierarchical decoder in order to model long- term musical structures. In our study, we explore applications of sparse representation such as de- noising musical ideas, unsupervised learning of composer styles, and music generation.

There are many applications such as:

-   Machine learning and data science
-   Astronomy
-   Artificial intelligence
-   Chemistry
-   Computational biology




## Problem Defenition

It is clear automatically varying the complexity of music has valuable applications. But how do we approach this problem without supervision? In words, we want to add or remove notes without diverging too much from the original "feeling" of music. In math we write:
> **Shift Invariant Dictionary Learning**:
>
>
>Given the data: $ X=\left[x_{1}, \ldots, x_{K}\right], x_{i} \in \mathbb{R}^{d} $. We want a dictionary $\mathbf{D} \in \mathbb{R}^{d \times n}: D=\left[d_{1}, \ldots, d_{n}\right]$ , and a representation $R=\left[r_{1}, \ldots, r_{K}\right], r_{i} \in \mathbb{R}^{n}$ such that the reconstruction $\|X-\mathbf{D} R\|_{F}^{2}$ is minimized and $r_{i}$ are sparsed. The optimization problem can be formulated as:
>
>$$\underset{\mathbf{D} \in \mathcal{C}, r_{i} \in \mathbb{R}^{n}, \lambda>0} {\operatorname{argmin}} \sum_{i=1}^{K}\left\|x_{i}-\mathbf{D} r_{i}\right\|_{2}^{2}+\lambda\left\|r_{i}\right\|_{0} \\   \mathcal{C} \equiv\left\{\mathbf{D} \in \mathbb{R}^{d \times n}:\left\|d_{i}\right\|_{2} \leq 1 \forall i=1, \ldots, n\right\} $$




## How do we solve this problem?

In order to reconstruct pitch vectors with the extra criteria of maintaining theoriginal chord/harmonic functionality, we propose a combined loss of MSE onpitch vector reconstruction and Cross Entropy on symbolic chord targets. Thereconstruction should be such that we do not lose the ability to map the originalchords but the information bottleneck serves to generalize pitch functionality




## Results

A linear program LP is a special instance of an SDP.
This means the LP can be written as an SDP

```{math}
\begin{aligned}
&\operatorname{minimize} \quad C \bullet X\\
&\begin{array}{ll}
\text { s.t. } & A_{i} \bullet X=b_{i}\quad i=1, \ldots, m \\
& X_{i j}=0 \quad i=1, \ldots, n   \quad j=i+1, \ldots, n \\
& X \succeq 0
\end{array}
\end{aligned}
```


```{math}
C=\left(\begin{array}{cccc}
c_{1} & 0 & \ldots & 0 \\
0 & c_{2} & \ldots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \ldots & c_{n}
\end{array}\right)
\quad
X=\left(\begin{array}{cccc}
x_{1} & 0 & \ldots & 0 \\
0 & x_{2} & \ldots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \ldots & x_{n}
\end{array}\right)
```


```{math}
\begin{aligned}
A_{i}=\left(\begin{array}{cccc}
a_{i 1} & 0 & \ldots & 0 \\
0 & a_{i 2} & \ldots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \ldots & a_{i n}
\end{array}\right) \quad   i=1, \ldots, m
\end{aligned}
```






## Numerical Example


















