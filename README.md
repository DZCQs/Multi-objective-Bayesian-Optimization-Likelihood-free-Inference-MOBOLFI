# Multi-objective Bayesian Optimization Likelihood-free Inference (MOBOLFI)

An implementation of the TMLR 2025 [paper](https://openreview.net/forum?id=hQjwDqfSzj): Multi-objective Bayesian optimization for Likelihood-Free inference in sequential sampling models of decision making. 

## Requirements

* Python >= 3.10
* Pytorch >= 2.0
* Botorch >= 0.13


## Structure

* [`toy_example/`](toy_example/): Implementation of Example on Sec 4.1 in the paper, which refers to Example 1 in [paper](https://arxiv.org/abs/2311.10671) by Schmitt et al [^1]. File ['experiment1_toy_example.ipynb'](toy_example/experiment1_toy_example.ipynb) implements MOBOLFI on this example, generates Figures 1, 2, 9 and 10 in paper.
* [`dcc/`](dcc/): Implementation of Example on Appendix D in the paper, which refers to Day care center example in [paper](http://www.jmlr.org/papers/v17/15-017.html) by Gutmann et al [^2]. File ['experiment2_dcc.ipynb'](dcc/experiment2_dcc.ipynb) implements MOBOLFI on this example, generates Figure 16 in paper.
* [`mlba_synthetic/`](mlba_synthetic/): Implementation of Example on Sec 4.2.2 and 4.2.3 in the paper, which uses synthetic data geenrated by MLBA simulator (see details on Sec 4.2.1). [`Data`](mlba_synthetic
/et_choice_resultf5.csv) consists of decision making data collected in the way discussed on Sec 4.2.4 in the paper. File ['experiment2_dcc.ipynb'](mlba_synthetic/experiment3_mlba.ipynb) implements MOBOLFI on this example, generates Figures 5, 6, 11, 12, 14 in paper. Folder [`mlba_synthetic/mlba_synthetic_AUX/`](mlba_synthetic/mlba_synthetic_AUX/) contains codes and outputs generating Figure 13.
* [`MLBA_empirical/`](MLBA_empirical/): Implementation of Example on Sec 4.2.4 in the paper, which uses the real data collected by our team (see details on Sec 4.2.4). File ['experiment4_MLBA_v2.ipynb'](MLBA_empirical/experiment4_MLBA_v2.ipynb) implements MOBOLFI on this example, generates Figures 7, 8, 15 in paper.


## Reproducing
Just download the .ipynb notebooks (and .csv data if needed) and run. After getting familar with the methodology, one can change the value of hyperparameters in these notebooks (including the num_init_samples, number_of_iterGPtraining, tol, etc).



## Contact with author
If you have any question regarding this paper, feel free the email me:
* `e1039688@u.nus.edu` -- David Chen



[^1] Schmitt, Marvin, Stefan T. Radev, and Paul-Christian Bürkner. "Fuse It or Lose It: Deep Fusion for Multimodal Simulation-Based Inference." arXiv preprint arXiv:2311.10671 (2023).
[^2] Gutmann, Michael U., and Jukka Corander. "Bayesian optimization for likelihood-free inference of simulator-based statistical models." Journal of Machine Learning Research 17.125 (2016): 1-47.
