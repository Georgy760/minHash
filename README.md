## Max Hash и Min Hash в Хешировании с Локально-Чувствительными Функциями (Locality-Sensitive Hashing, LSH)
<details>
  <summary>Читать</summary>

Max Hash и Min Hash - это два различных метода, используемых в контексте Хеширования с Локально-Чувствительными Функциями (LSH) для поиска схожих элементов в многомерных данных. Основное отличие между ними заключается в том, как они выполняют хеширование и как это влияет на процесс поиска схожих элементов:

### Max Hash (Максимальное Хеширование):

В методе Max Hash каждый хеш-бакет (bucket) в хеш-таблице содержит максимальное значение хеша среди всех элементов, попавших в этот бакет. Max Hash пытается максимизировать вероятность коллизии (попадания в один бакет) для схожих элементов, поскольку схожие элементы будут иметь более высокие хеш-значения и, таким образом, будут более вероятно оказываться в одном и том же бакете.

### Min Hash (Минимальное Хеширование):

В методе Min Hash каждый хеш-бакет в хеш-таблице содержит минимальное значение хеша среди всех элементов, попавших в этот бакет. Min Hash, наоборот, пытается минимизировать вероятность коллизии для схожих элементов, поскольку схожие элементы будут иметь более низкие хеш-значения и, таким образом, будут менее вероятно оказываться в одном и том же бакете.

Оба метода применяются в задачах поиска близких элементов, но выбор между Max Hash и Min Hash зависит от конкретных требований задачи и целей приложения:

- Max Hash может быть полезен, когда вы хотите максимизировать вероятность обнаружения схожих элементов, и вы готовы пожертвовать некоторой точностью. Это может быть полезно, например, при поиске схожих документов или изображений.

- Min Hash, наоборот, может быть полезен, когда вы хотите минимизировать вероятность ложных срабатываний и более важно избегать ошибок, чем находить все схожие элементы. Это может быть полезно, например, при поиске дубликатов в базе данных.
  
</details>

## Max Hash and Min Hash in Locality-Sensitive Hashing (LSH)
<details>
  <summary>Read</summary>

Max Hash and Min Hash are two different methods used in the context of Locality-Sensitive Hashing (LSH) to find similar items in multi-dimensional data. The main difference between them lies in how they perform hashing and how it affects the process of finding similar items:

### Max Hash (Maximum Hashing):

In Max Hash, each hash bucket in the hash table contains the maximum hash value among all elements that fall into that bucket. Max Hash attempts to maximize the collision probability (items landing in the same bucket) for similar items because similar items will have higher hash values and are thus more likely to end up in the same bucket.

### Min Hash (Minimum Hashing):

In Min Hash, each hash bucket in the hash table contains the minimum hash value among all elements that fall into that bucket. Min Hash, on the contrary, aims to minimize the collision probability for similar items because similar items will have lower hash values and are thus less likely to end up in the same bucket.

Both methods are used in tasks involving the search for close items, but the choice between Max Hash and Min Hash depends on the specific requirements of the task and the goals of the application:

- **Max Hash** can be useful when you want to maximize the probability of detecting similar items, and you are willing to sacrifice some accuracy. This can be helpful, for example, when searching for similar documents or images.

- **Min Hash**, on the other hand, can be useful when you want to minimize the probability of false positives and it is more important to avoid errors than to find all similar items. This can be useful, for example, when searching for duplicates in a database.

  
</details>
