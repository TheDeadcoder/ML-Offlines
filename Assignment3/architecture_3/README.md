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


