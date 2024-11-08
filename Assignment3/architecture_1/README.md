### Architecture 1

Architecture 1 consists of:
- **Input Layer**: 784 neurons (28x28 pixels flattened)
- **Hidden Layers**:
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

This configuration, with moderate dropout and adaptive learning rate, balances convergence speed and accuracy effectively for FashionMNIST classification.

---


