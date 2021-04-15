# translation_task

This is the translation task from the last interview.
Please try to implement a solution. Spend around 1 day of work into the task.  
Of course you can decide to spend more time on this task for a more sophisticated solution, but it is not necessary.  
In the end you will send me your solution and tell me your thoughts, why you implemented this the way you did and what you would work on if you had more time.
If you tried out an implementation and it didn't work, tell me that aswell, it's no problem if things don't work as long as you learn something new from it! :)

### example sentences

Example sentences are stored in the 'data_sentences.csv' file.
- there are 2 languages that we want to translate to: turkish and arabic.
- some sentences in data_sentences.csv have the same target sentence, some are slightly different (e.g. _where does it hurt_ and _does it hurt_)
- there are erronous sentences in the data
- this data is just a small example of possible real data. Keep that in mind when designing your solution

### Goal

The task is to find a way to create a translation functionality. You can either choose to hard-code (e.g. the target translation sentences) or use a third-party API.
If you hard-code things, however, you should keep in mind how to handle sentences that are out of scope or that you did not see in the _data_sentences.csv_ yet
More sophisticated solutions are also possible, it is up to you :)

- The translation functionality should be easily extendable for more languages
- The translation functionality should be easily extendable for more sentences
- The translation functionality should have error-handling (e.g. input data that is out of scope (yet), input data that does not make sense here, noisy data)
- you do **NOT** have to actually provide all the translations. It would be enough to simply classify the sentence and return something like "pain_sentence_turkish"

### Input Data

The input will be a string, you do __NOT__ have to read data from the .csv file with pandas or something.
But of course you can do that for your own testing purposes.
Just use the sentences as a string, e.g.
```
input_sentence = "hi dexter can you translate to turkish do you have diabetes"
```

### Output Data

The output will be a string. The return can be something like
```
output_sentence = "pain_sentence_turkish"
return output_sentence
```

### Other info

- the programming language is python
- you can use other libraries
- you can use external pretrained models (or train/fine-tune them yourself) or third-party APIs
- it is up to you how you want to implement it.