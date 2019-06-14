# Task 1 - Named Entity Recognation

The first task we propose is NER, the task of identifying proper nouns within a given text and classifying them into one of many relevant categories or within a default category known as Miscellaneous. Our objective with this task is to evaluate the proposed systems in many textual genres. For datasets that have as main textual genres: news, memorandums, e-mails, interviews and magazine articles, we will evaluate the following categories: PER – Person, PLC – Place, ORG – Organization, VAL – Value and TME – Time. On the other hand, for Clinical notes and Legal texts, of which we will only evaluate the PER – Person category.

## Run Evaluation

ATENÇÃO: O arquivo de saída de seu sistema deve conter um token especial para divisão dos dois datasets "StartSecondHAREM", tudo que há abaixo desse token pertence ao segundo HAREM e portanto apenas a categoria *Value*, ou seja, todas as outras categorias devem ser mapeadas para "O". Acima do token "StartSecondHAREM" a categoria *Value* deve ser mapeada para "O".

STEP 1: Clone this repository

STEP 3: Run our script

```python3 eval.py <output_of_your_system.txt> shDataset.txt <name_output_file_alignment.txt>```
