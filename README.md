# 02456_DeepLearning_Project

Group project in Course 02456 - Deep Learning 2026. Project in "Guidance of Autoregressive Protein Language Models"

# Overview

## Phase 1: Autoregressive models.

- Implement and train a simple MLP language model akin to Figure 1 in [2] that takes in the
  three previous tokens (amino acids) and predicts the next, using a deep learning framework
  such as PyTorch. The model architecture and hyperparameters are up to you, but clearly state
  and justify your choices in the report.
- Implement and train a recurrent neural network (RNN) model or a causal decoder-only multi-
  head attention Transformer model [3]. For the RNN choose between the vanilla RNN, Gated
  Recurrent Unit (GRU) or Long Short-Term Memory (LSTM). Like the MLP, the specific model
  design is up to you but needs to be explained and justified in the report.
- Evaluate and visualize the performance of these models by folding the generated sequences
  with ESMFold [4] and presenting relevant metrics (code for evaluation will be provided).

## Phase 2: Classifier guidance

- Select your trained RNN or Transformer, freeze the model weights, and then re-train a clas-
  sification head on top of the frozen model to predict the protein family. Remember, the head
  needs to be a noisy predictor such that it learns to predict the family membership even when
  it has seen only part of a sequence.
- Evaluate the overall performance of the predictive model on clean and partial finished se-
  quences.
- Perform guided generation towards one of the protein families using classifier guidance. Try
  varying λ to see the effect of guidance.

## Phase 3: Classifier-free guidance

- Train a conditioned version of your selected autoregressive architecture, using label dropout
  so that the same network also learns both unconditional and conditional generation. Use this
  model to investigate classifier-free guidance.
- Evaluate and visualize the performance of the guided and unguided models (classifier and
  classifier-free guidance). Investigate whether guidance increases membership in the target
  4
  family while retaining the model’s ability to generate realistic protein structures, and to char-
  acterize the trade-off between the two. Use the predictive model to report predicted target-
  family membership. Discuss the limitations of evaluating classifier-guided samples using the
  same predictor that guided their generation.
- Discuss what the difficulties are when evaluating generated data. How do we know the gener-
  ated data is ”good”?

##
