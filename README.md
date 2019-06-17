# Task 1 - Named Entity Recognation

The first task we propose is NER, the task of identifying proper nouns within a given text and classifying them into one of many relevant categories or within a default category known as Miscellaneous. Our objective with this task is to evaluate the proposed systems in many textual genres. For datasets that have as main textual genres: news, memorandums, e-mails, interviews and magazine articles, we will evaluate the following categories: PER – Person, PLC – Place, ORG – Organization, VAL – Value and TME – Time. On the other hand, for Clinical notes and Legal texts, of which we will only evaluate the PER – Person category.

## Run Evaluation

ATENÇÃO: O arquivo de saída de seu sistema deve conter um token especial para divisão dos dois datasets "StartSecondHAREM", tudo que há abaixo desse token pertence ao segundo HAREM e portanto apenas a categoria *Value*, ou seja, todas as outras categorias devem ser mapeadas para "O". Acima do token "StartSecondHAREM" a categoria *Value* deve ser mapeada para "O". Nós fizemos manualmente estas mudanças para cada participante e usamos o algoritmo *v1EvaluationAlgorithm*. Entretanto, também disponibilizamos um script *v2EvaluationAlgorithm* que faz automaticamente as alterações necessárias.

**Caso faça manualmente as alterações:**

STEP 1: Faça as mudanças já orientadas acima. Você pode usar um editor como o Sublime Text 3;

STEP 2: Clone this repository;

STEP 3: In TASK1 folder run our script:

```python3 v1EvaluationAlgorithm.py <output_of_your_system.txt> shDataset.txt <name_output_file_alignment.txt>```

**Para as mudanças automáticas:**

STEP 1: Clone this repository;

STEP 2: In TASK1 folder run our script:

```python3 v2EvaluationAlgorithm.py <output_of_your_system.txt> shDataset.txt <name_output_file_alignment.txt>```

# Task 2 - Relation Extraction for Named Entities

We propose a RE task that involves the automatic extraction of any relation descriptor expressing any type of relation between a pair of Named Entities of the Person, Place and Organization categories in Portuguese language texts.

## Run Evaluation

STEP 1: Clone this repository;

STEP 2: In TASK2 folder, run our script:

```python3 ```
