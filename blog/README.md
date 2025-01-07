# [Not All Tokens Are What You Need for Pretraining](https://openreview.net/forum?id=0NMzBwqaAJ)

---

### Team Members:

- Nazmus Sakib (1905061)
- Protoy Barai (1905068)
- Ahmed Farhan Shahriar Chowdhury (1905081)

## Problem Addressed in the Paper:

The central problem addressed in the paper is that traditional language model pretraining uniformly applies a next-token prediction loss to all tokens in the training corpus. This approach assumes that all tokens are equally important for model learning, but the authors challenge this assumption. They argue that:

- **Noisy and Ineffective Tokens**: Pretraining corpora, even after extensive filtering, contain noisy and irrelevant tokens. Training on these tokens can waste computational resources and reduce the model's ability to focus on learning meaningful patterns.

- **Token Dynamics**: Not all tokens contribute equally to model training. The study categorizes tokens based on their training loss trajectories, such as:

  - **Easy Tokens**: Tokens that are quickly learned and contribute little to further training.
  - **Hard Tokens**: Tokens that resist convergence and show fluctuating or high loss throughout training.
  - **Ambiguous Tokens**: Tokens that are noisy or poorly aligned with the desired learning objectives.

<br>

<p align="center">
  <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/14/undesired_token.png" width="80%" />
</p>

<br>

- **Inefficiency in Uniform Loss Application**: Applying the same loss function to all tokens leads to inefficient training, as valuable compute is spent on unimportant or already-learned tokens.


## Importance:

- **Efficiency in Pretraining**:As LLMs scale, pretraining them involves massive computational costs. Addressing token-level inefficiencies can significantly reduce these costs while maintaining or even improving performance.

- **Data Quality and Distribution**: The mismatch between the natural distribution of web data and the ideal distribution for downstream applications necessitates selective training on tokens aligned with target applications.

- **Performance on Downstream Tasks**: Focusing on the most impactful tokens can enhance the model’s performance in specific tasks, particularly those requiring reasoning or domain-specific knowledge, such as mathematics.

- **Resource Optimization**: With the growing size of datasets (often in billions of tokens), optimizing the selection of tokens for pretraining can help small-scale researchers and organizations who lack resources for massive-scale training.

## Key Contributions & Methodology:

- **Analysis of Token-Level Training Dynamics**:

  - The authors examine how individual token losses evolve during pretraining, identifying distinct patterns among tokens. They categorize tokens into four groups based on loss trajectories:
    - **H→H (High to High)**:Tokens with consistently high loss, indicating persistent difficulty.
    - **L→H (Low to High)**: Tokens whose loss increases over time, suggesting emerging challenges.
    - **H→L (High to Low)**:Tokens with decreasing loss, showing effective learning.
    - **L→L (Low to Low)**: Tokens with consistently low loss, indicating they are easily learned or redundant.
    <br>

    <p align="center">
      <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/14/token_dynamics.png" width="80%" />
    </p>

    <br>
  - This analysis reveals that a significant portion of tokens either remain challenging or are quickly learned, implying that uniform training across all tokens is inefficient.

- **Introduction of Selective Language Modeling (SLM):**

  - SLM selectively trains on tokens deemed most beneficial for learning, aligning the training process with desired data distributions. The process involves:

    - Reference Model Training
    - Token Scoring: Tokens are scored based on their excess loss, defined as the difference between the current training model’s loss.

    - Selective Training: The language model is trained only on tokens that fall within the top k% of excess loss scores. The SLM objective modifies the standard cross-entropy loss to focus on selected tokens. 
    <br>

    <p align="center">
      <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/14/slm_model.png" width="80%" />
    </p>

    <br>

- **Development of the Rho-1 Language Model**:

  - The authors implement SLM in the Rho-1 language model, demonstrating its effectiveness through continual pretraining on both specialized and general corpora.
  - When pretrained on the 15B token OpenWebMath corpus, Rho-1 shows significant improvements in few-shot accuracy across multiple math tasks.
  - After fine-tuning, Rho-1 models achieve state-of-the-art results on the MATH dataset, matching the performance of models like DeepSeekMath while utilizing only 3% of the pretraining tokens.
  - Pretraining on an 80B token general corpus results in an average enhancement across diverse tasks, indicating the broad applicability of SLM.

## Results:

- **Mathematical Pretraining Results**:

  - **Rho-1** models pretrained on the **OpenWebMath** corpus showed significant improvements in few-shot reasoning tasks.
  - **Few-Shot Accuracy**:
    - Rho-1 models pretrained on the OpenWebMath corpus showed significant improvements in **few-shot reasoning** tasks.
    - These results match the performance of DeepSeekMath models, which require up to **10x** more training tokens.
  - **Efficiency Gains**: Rho-1 models reached baseline performance up to **10x faster** than traditional causal language modeling (CLM) baselines.
  <br>

    <p align="center">
      <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/14/math-2.png" width="80%" />
    </p>

  <br>

- **General Pretraining Results**: By applying SLM to a general corpus of 80B tokens, Rho-1 achieved significant improvements across 15 diverse benchmarks:

  - **Average improvement:** 6.8%
  - Notable gains were observed in code-related and **mathematical tasks**, exceeding **10%** improvements in these areas.
  <br>

    <p align="center">
      <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/14/general_task.png" width="80%" />
    </p>

  <br>

- **Self-Reference Experiments**:

  - Even using a subset of the OpenWebMath corpus, SLM achieved a **2.4%** improvement in downstream task accuracy.
  - By combining two scoring functions (reference model loss and token entropy), the method improved performance by 3.3% while reducing token usage by 40%.
  <br>

    <p align="center">
      <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/14/efficient.png" width="90%" />
    </p>

  <br>

- **Ablation Studies**:
  - **Effect of Token Selection Ratio**: selecting approximately **60-70% of tokens** (based on excess loss scores) provided the optimal balance between efficiency and performance.
  - **Correlation with Downstream Performance**: Tokens selected by SLM had a stronger correlation with downstream task performance compared to unselected tokens.

## Insights, Application & Future direction:

### Key-Insights: 

- **Token Level Dynamics**, which states that not all tokens contribute equally to model training. Based on loss trajectory, they divide the tokens into several categories

- **Efficiency Through Selectivity**, which states that the **Selective Language Modeling (SLM)** technique selectively trains on high-utility tokens, which have the greatest impact on model learning. This challenges the conventional approach of treating all tokens equally during pretraining.

- By focusing on valuable tokens, the proposed **RHO-1** model achieves substantial improvements in both **math-specific** tasks and **general domain** tasks, while using fewer tokens and resources.

### Application-fields

- **Mathematical Reasoning**: RHO-1 shows exceptional improvements on tasks like **MATH** and **GSM8k**, making it a promising approach for developing advanced models for scientific computation and educational tools.
  <br>

    <p align="center">
      <img src="https://ycjfhirkrwhkotpadfln.supabase.co/storage/v1/object/public/statics/14/math.png" width="80%" />
    </p>

  <br>
- **General Language Model Training**: SLM can be applied to general pretraining tasks, such as creating **data-efficient general-purpose language models** for NLP applications like chatbots, search engines, and document summarization.
- **Data Optimization in Low-Resource Settings**: SLM’s ability to work with smaller token subsets makes it suitable for organizations with **limited access to high-quality datasets or computational resources**.
- **Token-Based Filtering in Large Datasets**: SLM’s methodology can assist in **curating cleaner datasets** for training, removing noise from data pipelines while retaining meaningful information.

### Future Scopes:

- **Expanding Beyond Math**: Investigate SLM's performance on other specialized domains like **medicine**, **legal reasoning**, and **creative content generation**.
- **Token Utility Metrics**: Explore more sophisticated methods for evaluating token utility. Current approaches rely on excess loss; future work could incorporate additional metrics like **semantic relevance**, **contextual diversity**, or **domain-specific features**.
- **Scalability**: Study how SLM scales to **larger models (e.g., 100B+ parameters)** and tasks requiring extreme generalization, such as GPT-level models.
- **Long-Term Effects on Fine-Tuning**: Assess the impact of SLM-pretrained models on downstream fine-tuning tasks, especially those requiring reasoning and multi-step problem-solving.
