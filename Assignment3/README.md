# Neural Network Model

## Introduction

This project implements a Feed-Forward Neural Network (FNN) from scratch for classifying the FashionMNIST dataset. The model is trained using various configurations of learning rates and dropout, focusing on optimizing performance while avoiding overfitting.

The FashionMNIST dataset consists of 70,000 grayscale images of size 28x28 pixels, categorized into 10 classes of apparel such as T-shirts, trousers, and shoes. Our goal is to develop an efficient and accurate model for this classification task.

---

## Model Architecture

### Architecture 1

Architecture 1 consists of:
- **Input Layer**: 784 neurons (28x28 pixels flattened)
- **Hidden Layers**:
  - **Dense Layer**: 512 units + Batch Normalization + ReLU + Dropout
  - **Dense Layer**: 256 units + Batch Normalization + ReLU + Dropout
  - **Dense Layer**: 128 units + Batch Normalization + ReLU + Dropout
- **Output Layer**: 10 units with Softmax for classification

**Regularization**: Dropout with varying rates (default set to 0.4).

---

## Training Configuration

The model was trained using **three different learning rates** (0.005, 0.001, 0.0009, and 0.0006) to explore the optimal setup for model convergence and accuracy.

### Hyperparameters
- **Optimizer**: Adam
- **Batch Size**: 64
- **Number of Epochs**: 25
- **Dropout Rate**: 0.4
- **Learning Rates Tested**: 0.005, 0.001, 0.0009, 0.0006

---

## Training Results

Below are the results for each learning rate configuration, detailing training and validation metrics across 25 epochs.

### Learning Rate: 0.005

| Epoch | Training Loss | Training Accuracy | Training F1 | Validation Loss | Validation Accuracy | Validation F1 |
|-------|---------------|-------------------|-------------|-----------------|---------------------|---------------|
| 1     | 0.5565        | 80.08%           | 0.7989      | 0.3970          | 85.10%             | 0.8485        |
| 2     | 0.4408        | 84.21%           | 0.8410      | 0.3622          | 86.70%             | 0.8634        |
| ...   | ...           | ...              | ...         | ...             | ...                | ...           |
| 25    | 0.2087        | 92.26%           | 0.9223      | 0.2789          | 90.52%             | 0.9066        |

**Test Results**:
- **Test Loss**: 0.2767
- **Test Accuracy**: 90.42%
- **Test F1 Score**: 0.9042

#### Plots for Learning Rate 0.005
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/loss_Arch1_lr_0.005.png" width="45%" alt="Loss vs Epochs (LR 0.005)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/accuracy_Arch1_lr_0.005.png" width="45%" alt="Accuracy vs Epochs (LR 0.005)">
</p>
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/f1_Arch1_lr_0.005.png" width="45%" alt="F1 Score vs Epochs (LR 0.005)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/confusion_matrix_Arch1_lr_0.005.png" width="45%" alt="Confusion Matrix (LR 0.005)">
</p>

---

### Learning Rate: 0.001

| Epoch | Training Loss | Training Accuracy | Training F1 | Validation Loss | Validation Accuracy | Validation F1 |
|-------|---------------|-------------------|-------------|-----------------|---------------------|---------------|
| 1     | 0.5835        | 79.38%           | 0.7922      | 0.3601          | 86.62%             | 0.8662        |
| 2     | 0.4285        | 84.52%           | 0.8441      | 0.3354          | 87.70%             | 0.8790        |
| ...   | ...           | ...              | ...         | ...             | ...                | ...           |
| 25    | 0.1976        | 92.59%           | 0.9255      | 0.2687          | 90.23%             | 0.9039        |

**Test Results**:
- **Test Loss**: 0.2744
- **Test Accuracy**: 90.47%
- **Test F1 Score**: 0.9050

#### Plots for Learning Rate 0.001
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/2/loss_Arch1_lr_0.001.png" width="45%" alt="Loss vs Epochs (LR 0.001)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/2/accuracy_Arch1_lr_0.001.png" width="45%" alt="Accuracy vs Epochs (LR 0.001)">
</p>
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/2/f1_Arch1_lr_0.001.png" width="45%" alt="F1 Score vs Epochs (LR 0.001)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/2/confusion_matrix_Arch1_lr_0.001.png" width="45%" alt="Confusion Matrix (LR 0.001)">
</p>

---

### Learning Rate: 0.0009

| Epoch | Training Loss | Training Accuracy | Training F1 | Validation Loss | Validation Accuracy | Validation F1 |
|-------|---------------|-------------------|-------------|-----------------|---------------------|---------------|
| 1     | 0.5883        | 79.37%           | 0.7918      | 0.3738          | 86.12%             | 0.8623        |
| 2     | 0.4361        | 84.31%           | 0.8420      | 0.3440          | 87.45%             | 0.8736        |
| ...   | ...           | ...              | ...         | ...             | ...                | ...           |
| 25    | 0.1975        | 92.72%           | 0.9268      | 0.2925          | 90.20%             | 0.9035        |

**Test Results**:
- **Test Loss**: 0.2808
- **Test Accuracy**: 90.30%
- **Test F1 Score**: 0.9030

#### Plots for Learning Rate 0.0009
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/3/loss_Arch1_lr_0.0009.png" width="45%" alt="Loss vs Epochs (LR 0.0009)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/3/accuracy_Arch1_lr_0.0009.png" width="45%" alt="Accuracy vs Epochs (LR 0.0009)">
</p>
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/3/f1_Arch1_lr_0.0009.png" width="45%" alt="F1 Score vs Epochs (LR 0.0009)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/3/confusion_matrix_Arch1_lr_0.0009.png" width="45%" alt="Confusion Matrix (LR 0.0009)">
</p>

---

### Learning Rate: 0.0006

| Epoch | Training Loss | Training Accuracy | Training F1 | Validation Loss | Validation Accuracy | Validation F1 |
|-------|---------------|-------------------|-------------|-----------------|---------------------|---------------|
| 1     | 0.6285        | 78.06%           | 0.7788      | 0.3802          | 85.72%             | 0.8543        |
| 2     | 0.4451        | 84.11%           | 0.8399      | 0.3638          | 86.42%             | 0.8664        |
| ...   | ...           | ...              | ...         | ...             | ...                | ...           |
| 25    | 0.1957        | 92.69%           | 0.9265      | 0.2770          | 90.15%             | 0.9033        |

**Test Results**:
- **Test Loss**: 0.2760
- **Test Accuracy**: 90.37%
- **Test F1 Score**: 0.9039

#### Plots for Learning Rate 0.0006
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/4/loss_Arch1_lr_0.0006.png" width="45%" alt="Loss vs Epochs (LR 0.0006)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/4/accuracy_Arch1_lr_0.0006.png" width="45%" alt="Accuracy vs Epochs (LR 0.0006)">
</p>
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/4/f1_Arch1_lr_0.0006.png" width="45%" alt="F1 Score vs Epochs (LR 0.0006)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/4/confusion_matrix_Arch1_lr_0.0006.png" width="45%" alt="Confusion Matrix (LR 0.0006)">
</p>

---

## Summary of Results

| Learning Rate | Test Loss | Test Accuracy | Test F1 Score |
|---------------|-----------|---------------|---------------|
| 0.005         | 0.2767    | 90.42%        | 0.9042        |
| 0.001         | 0.2744    | 90.47%        | 0.9050        |
| 0.0009        | 0.2808    | 90.30%        | 0.9030        |
| 0.0006        | 0.2760    | 90.37%        | 0.9039        |

The best test performance was achieved with **learning rate = 0.001**, yielding:
- **Test Accuracy**: 90.47%
- **Test F1 Score**: 0.9050

---

### Architecture 2

Architecture 2 consists of:
- **Input Layer**: 784 neurons (28x28 pixels flattened)
- **Hidden Layers**:
  - **Dense Layer**: 1024 units + Batch Normalization + ReLU + Dropout
  - **Dense Layer**: 512 units + Batch Normalization + ReLU + Dropout
  - **Dense Layer**: 256 units + Batch Normalization + ReLU + Dropout
  - **Dense Layer**: 128 units + Batch Normalization + ReLU + Dropout
- **Output Layer**: 10 units with Softmax for classification

**Regularization**: Dropout with varying rates (default set to 0.3).

---

## Training Configuration

The model was trained using **three different learning rates** (0.005, 0.001, 0.0009, and 0.0006) to explore the optimal setup for model convergence and accuracy.

### Hyperparameters
- **Optimizer**: Adam
- **Batch Size**: 64
- **Number of Epochs**: 25
- **Dropout Rate**: 0.3
- **Learning Rates Tested**: 0.005, 0.001, 0.0009, 0.0006

---

## Training Results

Below are the results for each learning rate configuration, detailing training and validation metrics across 25 epochs.

### Learning Rate: 0.005
| Epoch | Training Loss | Training Accuracy | Training F1 | Validation Loss | Validation Accuracy | Validation F1 |
|-------|---------------|-------------------|-------------|-----------------|---------------------|---------------|
| 1     | 0.5739        | 79.68%           | 0.7945      | 0.3818          | 85.60%             | 0.8561        |
| 2     | 0.4481        | 84.19%           | 0.8406      | 0.3452          | 87.25%             | 0.8719        |
| ...   | ...           | ...              | ...         | ...             | ...                | ...           |
| 25    | 0.1970        | 92.80%           | 0.9276      | 0.2960          | 89.63%             | 0.8995        |

**Test Results**:
- **Test Loss**: 0.2919
- **Test Accuracy**: 89.74%
- **Test F1 Score**: 0.8985

#### Plots for Learning Rate 0.005
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/5/loss_Arch2_lr_0.005.png" width="45%" alt="Loss vs Epochs (LR 0.005)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/5/accuracy_Arch2_lr_0.005.png" width="45%" alt="Accuracy vs Epochs (LR 0.005)">
</p>
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/5/f1_Arch2_lr_0.005.png" width="45%" alt="F1 Score vs Epochs (LR 0.005)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/5/confusion_matrix_Arch2_lr_0.005.png" width="45%" alt="Confusion Matrix (LR 0.005)">
</p>

---

### Learning Rate: 0.001

| Epoch | Training Loss | Training Accuracy | Training F1 | Validation Loss | Validation Accuracy | Validation F1 |
|-------|---------------|-------------------|-------------|-----------------|---------------------|---------------|
| 1     | 0.5955        | 79.41%           | 0.7917      | 0.3628          | 86.62%             | 0.8653        |
| 2     | 0.4321        | 84.56%           | 0.8443      | 0.3320          | 87.83%             | 0.8802        |
| ...   | ...           | ...              | ...         | ...             | ...                | ...           |
| 25    | 0.1845        | 93.18%           | 0.9315      | 0.2811          | 90.63%             | 0.9070        |

**Test Results**:
- **Test Loss**: 0.2755
- **Test Accuracy**: 90.47%
- **Test F1 Score**: 0.9033

#### Plots for Learning Rate 0.001
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/6/loss_Arch2_lr_0.001.png" width="45%" alt="Loss vs Epochs (LR 0.001)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/6/accuracy_Arch2_lr_0.001.png" width="45%" alt="Accuracy vs Epochs (LR 0.001)">
</p>
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/6/f1_Arch2_lr_0.001.png" width="45%" alt="F1 Score vs Epochs (LR 0.001)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/6/confusion_matrix_Arch2_lr_0.001.png" width="45%" alt="Confusion Matrix (LR 0.001)">
</p>

---

### Learning Rate: 0.0009

| Epoch | Training Loss | Training Accuracy | Training F1 | Validation Loss | Validation Accuracy | Validation F1 |
|-------|---------------|-------------------|-------------|-----------------|---------------------|---------------|
| 1     | 0.5995        | 79.38%           | 0.7918      | 0.3649          | 86.80%             | 0.8700        |
| 2     | 0.4348        | 84.56%           | 0.8446      | 0.3325          | 88.23%             | 0.8823        |
| ...   | ...           | ...              | ...         | ...             | ...                | ...           |
| 25    | 0.1834        | 93.25%           | 0.9322      | 0.2922          | 89.90%             | 0.9014        |

**Test Results**:
- **Test Loss**: 0.2898
- **Test Accuracy**: 89.86%
- **Test F1 Score**: 0.8989

#### Plots for Learning Rate 0.0009
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/7/loss_Arch2_lr_0.0009.png" width="45%" alt="Loss vs Epochs (LR 0.0009)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/7/accuracy_Arch2_lr_0.0009.png" width="45%" alt="Accuracy vs Epochs (LR 0.0009)">
</p>
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/7/f1_Arch2_lr_0.0009.png" width="45%" alt="F1 Score vs Epochs (LR 0.0009)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/7/confusion_matrix_Arch2_lr_0.0009.png" width="45%" alt="Confusion Matrix (LR 0.0009)">
</p>

---

### Learning Rate: 0.0006

| Epoch | Training Loss | Training Accuracy | Training F1 | Validation Loss | Validation Accuracy | Validation F1 |
|-------|---------------|-------------------|-------------|-----------------|---------------------|---------------|
| 1     | 0.6249        | 78.66%           | 0.7849      | 0.3676          | 86.58%             | 0.8642        |
| 2     | 0.4413        | 84.39%           | 0.8428      | 0.3355          | 87.18%             | 0.8715        |
| ...   | ...           | ...              | ...         | ...             | ...                | ...           |
| 25    | 0.1845        | 93.21%           | 0.9318      | 0.3115          | 89.77%             | 0.8969        |

**Test Results**:
- **Test Loss**: 0.2981
- **Test Accuracy**: 89.86%
- **Test F1 Score**: 0.8967

#### Plots for Learning Rate 0.0006
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/8/loss_Arch2_lr_0.0006.png" width="45%" alt="Loss vs Epochs (LR 0.0006)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/8/accuracy_Arch2_lr_0.0006.png" width="45%" alt="Accuracy vs Epochs (LR 0.0006)">
</p>
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/8/f1_Arch2_lr_0.0006.png" width="45%" alt="F1 Score vs Epochs (LR 0.0006)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/8/confusion_matrix_Arch2_lr_0.0006.png" width="45%" alt="Confusion Matrix (LR 0.0006)">
</p>

---

## Summary of Results

| Learning Rate | Test Loss | Test Accuracy | Test F1 Score |
|---------------|-----------|---------------|---------------|
| 0.005         | 0.2919    | 89.74%        | 0.8985        |
| 0.001         | 0.2755    | 90.47%        | 0.9033        |
| 0.0009        | 0.2898    | 89.86%        | 0.8989        |
| 0.0006        | 0.2981    | 89.86%        | 0.8967        |

The best test performance was achieved with **learning rate = 0.001**, yielding:
- **Test Accuracy**: 90.47%
- **Test F1 Score**: 0.9033

This configuration, with moderate dropout and adaptive learning rate, balances convergence speed and accuracy effectively for FashionMNIST classification.

---
### Architecture 3

Architecture 3 consists of:
- **Input Layer**: 784 neurons (28x28 pixels flattened)
- **Hidden Layers**:
  - **Dense Layer**: 256 units + Batch Normalization + ReLU + Dropout
  - **Dense Layer**: 128 units + Batch Normalization + ReLU + Dropout
- **Output Layer**: 10 units with Softmax for classification

**Regularization**: Dropout with varying rates (default set to 0.3).

---

## Training Configuration

The model was trained using **three different learning rates** (0.005, 0.001, 0.0009, and 0.0006) to explore the optimal setup for model convergence and accuracy.

### Hyperparameters
- **Optimizer**: Adam
- **Batch Size**: 64
- **Number of Epochs**: 25
- **Dropout Rate**: 0.3
- **Learning Rates Tested**: 0.005, 0.001, 0.0009, 0.0006

---

## Training Results

Below are the results for each learning rate configuration, detailing training and validation metrics across 25 epochs.

### Learning Rate: 0.005

| Epoch | Training Loss | Training Accuracy | Training F1 | Validation Loss | Validation Accuracy | Validation F1 |
|-------|---------------|-------------------|-------------|-----------------|---------------------|---------------|
| 1     | 0.5420        | 80.67%           | 0.8053      | 0.3835          | 85.65%             | 0.8578        |
| 2     | 0.4264        | 84.54%           | 0.8444      | 0.3732          | 85.97%             | 0.8582        |
| ...   | ...           | ...              | ...         | ...             | ...                | ...           |
| 25    | 0.2225        | 91.67%           | 0.9162      | 0.2780          | 90.25%             | 0.9037        |

**Test Results**:
- **Test Loss**: 0.2782
- **Test Accuracy**: 90.30%
- **Test F1 Score**: 0.9026

#### Plots for Learning Rate 0.005
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/10/loss_Arch3_lr_0.005.png" width="45%" alt="Loss vs Epochs (LR 0.005)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/10/accuracy_Arch3_lr_0.005.png" width="45%" alt="Accuracy vs Epochs (LR 0.005)">
</p>
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/10/f1_Arch3_lr_0.005.png" width="45%" alt="F1 Score vs Epochs (LR 0.005)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/10/confusion_matrix_Arch3_lr_0.005.png" width="45%" alt="Confusion Matrix (LR 0.005)">
</p>

---

### Learning Rate: 0.001

| Epoch | Training Loss | Training Accuracy | Training F1 | Validation Loss | Validation Accuracy | Validation F1 |
|-------|---------------|-------------------|-------------|-----------------|---------------------|---------------|
| 1     | 0.5711        | 79.85%           | 0.7967      | 0.3716          | 86.32%             | 0.8640        |
| 2     | 0.4306        | 84.47%           | 0.8437      | 0.3425          | 86.95%             | 0.8722        |
| ...   | ...           | ...              | ...         | ...             | ...                | ...           |
| 25    | 0.2103        | 92.15%           | 0.9212      | 0.2683          | 90.48%             | 0.9062        |

**Test Results**:
- **Test Loss**: 0.2727
- **Test Accuracy**: 90.41%
- **Test F1 Score**: 0.9039

#### Plots for Learning Rate 0.001
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/11/loss_Arch3_lr_0.001.png" width="45%" alt="Loss vs Epochs (LR 0.001)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/11/accuracy_Arch3_lr_0.001.png" width="45%" alt="Accuracy vs Epochs (LR 0.001)">
</p>
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/11/f1_Arch3_lr_0.001.png" width="45%" alt="F1 Score vs Epochs (LR 0.001)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/11/confusion_matrix_Arch3_lr_0.001.png" width="45%" alt="Confusion Matrix (LR 0.001)">
</p>

---

### Learning Rate: 0.0009

| Epoch | Training Loss | Training Accuracy | Training F1 | Validation Loss | Validation Accuracy | Validation F1 |
|-------|---------------|-------------------|-------------|-----------------|---------------------|---------------|
| 1     | 0.5748        | 79.78%           | 0.7963      | 0.3892          | 85.63%             | 0.8553        |
| 2     | 0.4306        | 84.37%           | 0.8426      | 0.3393          | 87.57%             | 0.8755        |
| ...   | ...           | ...              | ...         | ...             | ...                | ...           |
| 25    | 0.2088        | 92.30%           | 0.9226      | 0.2807          | 90.07%             | 0.9030        |

**Test Results**:
- **Test Loss**: 0.2799
- **Test Accuracy**: 89.94%
- **Test F1 Score**: 0.9000

#### Plots for Learning Rate 0.0009
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/12/loss_Arch3_lr_0.0009.png" width="45%" alt="Loss vs Epochs (LR 0.0009)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/12/accuracy_Arch3_lr_0.0009.png" width="45%" alt="Accuracy vs Epochs (LR 0.0009)">
</p>
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/12/f1_Arch3_lr_0.0009.png" width="45%" alt="F1 Score vs Epochs (LR 0.0009)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/12/confusion_matrix_Arch3_lr_0.0009.png" width="45%" alt="Confusion Matrix (LR 0.0009)">
</p>

---

### Learning Rate: 0.0006

| Epoch | Training Loss | Training Accuracy | Training F1 | Validation Loss | Validation Accuracy | Validation F1 |
|-------|---------------|-------------------|-------------|-----------------|---------------------|---------------|
| 1     | 0.5981        | 79.04%           | 0.7883      | 0.3923          | 85.63%             | 0.8588        |
| 2     | 0.4394        | 84.28%           | 0.8416      | 0.3428          | 87.37%             | 0.8764        |
| ...   | ...           | ...              | ...         | ...             | ...                | ...           |
| 25    | 0.2137        | 91.95%           | 0.9190      | 0.2776          | 89.67%             | 0.8990        |

**Test Results**:
- **Test Loss**: 0.2833
- **Test Accuracy**: 89.90%
- **Test F1 Score**: 0.8996

#### Plots for Learning Rate 0.0006
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/13/loss_Arch3_lr_0.0006.png" width="45%" alt="Loss vs Epochs (LR 0.0006)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/13/accuracy_Arch3_lr_0.0006.png" width="45%" alt="Accuracy vs Epochs (LR 0.0006)">
</p>
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/13/f1_Arch3_lr_0.0006.png" width="45%" alt="F1 Score vs Epochs (LR 0.0006)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/13/confusion_matrix_Arch3_lr_0.0006.png" width="45%" alt="Confusion Matrix (LR 0.0006)">
</p>

---

## Summary of Results

| Learning Rate | Test Loss | Test Accuracy | Test F1 Score |
|---------------|-----------|---------------|---------------|
| 0.005         | 0.2782    | 90.30%        | 0.9026        |
| 0.001         | 0.2727    | 90.41%        | 0.9039        |
| 0.0009        | 0.2799    | 89.94%        | 0.9000        |
| 0.0006        | 0.2833    | 89.90%        | 0.8996        |

The best test performance was achieved with **learning rate = 0.001**, yielding:
- **Test Accuracy**: 90.41%
- **Test F1 Score**: 0.9039

This configuration, with moderate dropout and adaptive learning rate, balances convergence speed and accuracy effectively for FashionMNIST classification.

---


# Model Evaluation Summary

## Best Model

**Architecture**: Arch1  
**Learning Rate**: 0.001  

| Metric       | Value   |
|--------------|---------|
| **Test Accuracy**  | 90.47% |
| **Test F1 Score**  | 0.9050 |

The best model achieved a test accuracy of **90.47%** and a test F1 score of **0.9050**. This model, based on Architecture 1 and a learning rate of 0.001, demonstrates strong performance on the FashionMNIST dataset.

---

<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/9/loss_Arch1_lr_0.001.png" width="45%" alt="Loss vs Epochs (Best Model)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/9/accuracy_Arch1_lr_0.001.png" width="45%" alt="Accuracy vs Epochs (Best Model)">
</p>
<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/9/f1_Arch1_lr_0.001.png" width="45%" alt="F1 Score vs Epochs (Best Model)">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/9/confusion_matrix_Arch1_lr_0.001.png" width="45%" alt="Confusion Matrix (Best Model)">
</p>

### Performance Plots
The plots above show the performance of the best model (Arch1, LR=0.001) across epochs, including:
1. **Loss vs Epochs**: Training and validation loss convergence.
2. **Accuracy vs Epochs**: Progression of training and validation accuracy.
3. **F1 Score vs Epochs**: Training and validation F1 scores.
4. **Confusion Matrix**: Final test set confusion matrix, showing detailed classification results.

---

## Overall Test Accuracies


| Architecture | Layer  | Units | Components                                      |
|--------------|--------|-------|--------------------------------------------------|
| **Arch1**    | Input  | 784   | Flatten (28x28 images)                          |
|              | Layer 1| 512   | Batch Normalization, ReLU, Dropout               |
|              | Layer 2| 256   | Batch Normalization, ReLU, Dropout               |
|              | Layer 3| 128   | Batch Normalization, ReLU, Dropout               |
|              | Output | 10    | Softmax for classification                       |
| **Arch2**    | Input  | 784   | Flatten (28x28 images)                          |
|              | Layer 1| 1024  | Batch Normalization, ReLU, Dropout               |
|              | Layer 2| 512   | Batch Normalization, ReLU, Dropout               |
|              | Layer 3| 256   | Batch Normalization, ReLU, Dropout               |
|              | Layer 4| 128   | Batch Normalization, ReLU, Dropout               |
|              | Output | 10    | Softmax for classification                       |
| **Arch3**    | Input  | 784   | Flatten (28x28 images)                          |
|              | Layer 1| 256   | Batch Normalization, ReLU, Dropout               |
|              | Layer 2| 128   | Batch Normalization, ReLU, Dropout               |
|              | Output | 10    | Softmax for classification                       |

---

The following table below shows the test accuracies of each model configuration, organized by architecture and learning rate.

| Architecture | Learning Rate | Test Accuracy | Test F1 Score |
|--------------|---------------|---------------|---------------|
| Arch1        | 0.005         | 90.42%        | 0.9042        |
| **Arch1**    | **0.001**     | **90.47%**    | **0.9050**    |
| Arch1        | 0.0009        | 90.30%        | 0.9030        |
| Arch1        | 0.0006        | 90.37%        | 0.9039        |
| Arch2        | 0.005         | 89.74%        | 0.8985        |
| Arch2        | 0.001         | 90.47%        | 0.9033        |
| Arch2        | 0.0009        | 89.86%        | 0.8989        |
| Arch2        | 0.0006        | 89.86%        | 0.8967        |
| Arch3        | 0.005         | 90.30%        | 0.9026        |
| Arch3        | 0.001         | 90.41%        | 0.9039        |
| Arch3        | 0.0009        | 89.94%        | 0.9000        |
| Arch3        | 0.0006        | 89.90%        | 0.8996        |

---

### Conclusion

The best-performing models for this task were derived from **Architecture 1** with a learning rate of **0.001**, yielding consistent and high test accuracy and F1 scores. This architecture provides a good balance between complexity and generalization, making it well-suited for the FashionMNIST dataset.




