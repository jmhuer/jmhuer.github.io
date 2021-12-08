#!/usr/bin/env python
# coding: utf-8

# # Shift-Invariant Dictionary Learning using Temporal CONV-WTA Autoencoders for Discovering Music Relations
# 
#  <sub> <a href="https://jmhuer.github.io/mini_book/_build/html/docs/portfolio.html" style="color: red; text-decoration: underline;text-decoration-style: dotted;">← Back to Projects</a> </sub>
# 
# <img src="../../../../images/sidl.png" align="center"/>
# 
# <br>
# 
# The temporal structure of music is full of shift-invariant patterns (e.g. motifs, ostinatos, loops, etc.). We propose using a Tempo- ral Convolutional Winner-Take-All (CONV- WTA) autoencoder to find a shift-invariant dictionary to represent symbolic, multivariate, musical signals. The model learns to represent fixed length drum beats and variable length pi- ano music. We discuss applications of this sparse representation such as de-noising musi- cal ideas, unsupervised learning of composer styles, and music generation. To assist in re- lated work we include interactive code along with the trained models
# 
# 
# ## Introduction
# ---
# 
# The dictionary learning framework aims at finding a sparse representation of the input data (sparse coding) in the form of a linear combination of ba- sic elements called atoms. In doing so, sparse coding enables faster inference and easier inter- pretability thanks to its lightweight stored mem- ory, encoding of prior knowledge in the sparsity patterns, and discerning patterns in an informed and principled manner.
# Sparse dictionary learning has led to state-of-art results in various tasks including image and video processing, texture synthesis (Peyre ́, 2009), and unsupervised clustering (Ram ́ırez et al., 2010). In evaluations with the Bag-of-Words model (Ko- niusz et al., 2017), sparse coding was found empir- ically to outperform other coding approaches on category recognition tasks.
# When applied to music, the ability to distill complex data structures down to sets of dictio- naries—salient features of a specific performer or music, has a multitude of applications. Music transcription and classification tasks have seen a strong usage of sparse dictionary learning in the past (Grosse et al., 2007) (Costantini et al., 2013), (Blumensath and Davies, 2006), (Srinivas M et al., 2014), (Srinivas et al., 2014), (Cogliati et al., 2016). Nonetheless, we have yet to see a study that harnesses the advantages of sparse representa- tion for the purpose of music creation. Instead, the popular methods for discovering music relations and achieving music generation have been a trans- former with some sort of attention mechanism or other recurrent architectures. For instance, (Jiang Junyan et al., 2020) uses an attention module that is tailored to the discovery of sequence level rela- tions in music, while studies like (Roberts et al., 2018) uses the recurrent variational autoencoder and a hierarchical decoder in order to model long- term musical structures. In our study, we explore applications of sparse representation such as de- noising musical ideas, unsupervised learning of composer styles, and music generation.
# 
# There are many applications such as:
# 
# -   Unsupervised Style Discovery
# -   Composition Interpolation
# -   Music Decomposition
# 
# 
# 
# ## Problem Defenition
# ---
# 
# It is clear automatically varying the complexity of music has valuable applications. But how do we approach this problem without supervision? In words, we want to add or remove notes without diverging too much from the original "feeling" of music. In math we write:
# > **Shift Invariant Dictionary Learning**:
# >
# >
# >Given the data: $ X=\left[x_{1}, \ldots, x_{K}\right], x_{i} \in \mathbb{R}^{d} $. We want a dictionary $\mathbf{D} \in \mathbb{R}^{d \times n}: D=\left[d_{1}, \ldots, d_{n}\right]$ , and a representation $R=\left[r_{1}, \ldots, r_{K}\right], r_{i} \in \mathbb{R}^{n}$ such that the reconstruction $\|X-\mathbf{D} R\|_{F}^{2}$ is minimized and $r_{i}$ are sparsed. The optimization problem can be formulated as:
# >
# >$$\underset{\mathbf{D} \in \mathcal{C}, r_{i} \in \mathbb{R}^{n}, \lambda>0} {\operatorname{argmin}} \sum_{i=1}^{K}\left\|x_{i}-\mathbf{D} r_{i}\right\|_{2}^{2}+\lambda\left\|r_{i}\right\|_{0} \\   \mathcal{C} \equiv\left\{\mathbf{D} \in \mathbb{R}^{d \times n}:\left\|d_{i}\right\|_{2} \leq 1 \forall i=1, \ldots, n\right\} $$
# 
# 
# 
# 
# ## How do we solve this problem?
# ---
# 
# In order to reconstruct pitch vectors with the extra criteria of maintaining theoriginal chord/harmonic functionality, we propose a combined loss of MSE onpitch vector reconstruction and Cross Entropy on symbolic chord targets. Thereconstruction should be such that we do not lose the ability to map the originalchords but the information bottleneck serves to generalize pitch functionality
# 
# 
# ## Results
# ---
# 
# ### Visualization
# Below, are some of the results. To verify we have a good representation we can plot the top-2 components our encoded data
# 
# 
# <img src="../../../../images/pca.png" align="center"/>
# 
# 
# ### Interpolating Drum Data
# 
# One way of generating new music is to interpolate latent space. There are various ways of doing this, but in essence you can think about a convex convination between n examples. For our example we simply average sparse code between two examples:
# 
# 
# **Original 1**
# 
# <audio controls>
#   <source src="../../../../audio/sidl1.wav" type="audio/wav">
# Your browser does not support the audio element.
# </audio><br>
# <br>
# 
# **Original 2**
# 
# <audio controls>
#   <source src="../../../../audio/sidl2.wav" type="audio/wav">
# Your browser does not support the audio element.
# </audio><br>
# <br>
# 
# **Interpolated Result**
# 
# <audio controls>
#   <source src="../../../../audio/sidl3.wav" type="audio/wav">
# Your browser does not support the audio element.
# </audio><br>
# <br>
# 
# 
# 
# 
# ### Average Dictionary Activity
# 
# Finally another useful application for discovering style of a symbolic piece of music in an unsupervised way. To do this we average dictionary activity of arbitrary length music and plot main two compoenents:
# 
# <img src="../../../../images/sidl.png" align="center"/>
# 
# 
# ## Conclusion
# ---
# 
# We have shown that a Temporal CONV-WTA Autoencoder can learn a sparse representation of arbitrary length symbolic musical signal. This shift-invariant, sparse representation can be used to analyze features, de-noise, extract style, and to generate musical content in a structured or unstructured way. The reconstruction and generation for the drum (Groove) dataset was significantly better than the piano (MAESTRO) dataset. This is in part because the drum dataset was preprocessed to match with the kernel size, all drum sections were the same length, and had lower dimensionality in comparison. In the future, we hope to use a larger and more diverse dataset, improve reconstruction performance, and apply similar preprocessing to the piano data as done for the drum data. We also plan to further develop applications of this technology and build tools for artists.
