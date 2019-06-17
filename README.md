# Task 1 - Named Entity Recognition

The first task we propose is NER, the task of identifying proper nouns within a given text and classifying them into one of many relevant categories or within a default category known as Miscellaneous. Our objective with this task is to evaluate the proposed systems in many textual genres. For datasets that have as main textual genres: news, memorandums, e-mails, interviews and magazine articles, we will evaluate the following categories: PER – Person, PLC – Place, ORG – Organization, VAL – Value and TME – Time. On the other hand, for Clinical notes and Legal texts, of which we will only evaluate the PER – Person category.

## Run Evaluation

ATTENTION: The output of your system must contain a special token in order to divide both datasets "StartSecondHAREM", everything below this token belongs to the second HAREM and therefore only the category *Value*, in other words, all the other categories must be mapped to "O". Above the "StartSecondHAREM" token the category *Value* must be mapped to "O". We manually made this changes for each participant and used the script *v1EvaluationAlgorithm*. However, we also made available the script *v2EvaluationAlgorithm* that automatically do this changes.

**In case you manually change your output:**

STEP 1: Do the changes described above. You can use a text editor such as Sublime Text 3;

STEP 2: Clone this repository;

STEP 3: In TASK1 folder run our script:

```python3 v1EvaluationAlgorithm.py <output_of_your_system.txt> shDataset.txt <name_output_file_alignment.txt>```

**In case you want the changes to happen automatically:**

STEP 1: Clone this repository;

STEP 2: In TASK1 folder run our script:

```python3 v2EvaluationAlgorithm.py <output_of_your_system.txt> shDataset.txt <name_output_file_alignment.txt>```

# Task 2 - Relation Extraction for Named Entities

We propose a RE task that involves the automatic extraction of any relation descriptor expressing any type of relation between a pair of Named Entities of the Person, Place and Organization categories in Portuguese language texts.

## Run Evaluation

STEP 1: Clone this repository;

STEP 2: In TASK2 folder, run our script's help function for further instructions in how to use it:

```python avaliaIberLEFtask2.py --help```

# Citing our Paper
```
@article{ nerreiberlef2019,
author= {Sandra Collovini, Joaquim Santos, Bernardo Consoli, Juliano Terra, Renata Vieira,  Paulo Quaresma, Marlo Souza, Daniela Barreiro Claro, Rafael Glauber and Clarissa Castell\~a Xavier},
pages= {},
volume= {},
title= {Portuguese Named Entity Recognition and Relation Extraction Tasks at IberLEF 2019},
booktitle= {Proceedings of the Iberian Languages Evaluation Forum (IberLEF 2019)},
publisher= {CEUR-WS.org}, 
series= {CEUR Workshop Proceedings}, 
year= {2019} }
```
