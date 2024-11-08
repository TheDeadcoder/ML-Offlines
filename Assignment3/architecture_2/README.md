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


