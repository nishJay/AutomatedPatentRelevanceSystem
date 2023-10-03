# U-CREAT Pipeline Overview

![image](https://github.com/nishJay/AutomatedPatentRelevanceSystem/assets/77871395/b1a06ff2-4427-48d5-b593-332a1a4a94da)


## 1. Text Preprocessing
- **Roles:** Normalize text, clean noise, prepare for parsing.
- **Tasks:** 
  - Tokenization
  - Lemmatization
  - Part-of-Speech (POS) tagging
  - Named Entity Recognition (NER)

## 2. Event Extraction
- **Role:** Extract event tuples consisting of predicates and arguments.
- **Tasks:** 
  - Dependency parsing
  - Predicate and argument identification

## 3. Document Representation
- **Role:** Represent documents as sets/bags of events rather than raw words.
- **Tasks:** Store events extracted from each document.

## 4. Similarity Computation
- **Role:** Compare query and candidate events to calculate relevance.
- **Tasks:** Utilize various similarity metrics such as Jaccard, BM25, and cosine similarity.

## 5. Ranking Model
- **Role:** Rank candidate documents based on similarity scores.
- **Tasks:** Order candidates by their similarity to query events.

## 6. Evaluation
- **Role:** Evaluate retrieval performance using relevant metrics.
- **Tasks:** Compute precision, recall, and F1 score to assess system performance.

**In summary, the U-CREAT pipeline comprises the following key stages:**
1. **Text Preprocessing**
2. **Event Extraction**
3. **Event-based Document Representation**
4. **Computing Event Similarity**
5. **Ranking Candidates**
6. **Evaluating Rankings**

The core novel aspects of this pipeline are stages 2 and 3, which focus on extracting events from text and representing documents in terms of these events, providing a more nuanced understanding of the content beyond just words.
