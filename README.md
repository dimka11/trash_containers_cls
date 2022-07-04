# trash_containers_cls

Задача «Оптимизация работы коммунальных служб»

Качество снимков имеет три категории:

● неудовлетворительного качества;

● с отсутствующими мусорными баками;

● соответствующие всем необходимым условиям.


Описание входных значений
● train/ — папка, содержащая 543 фотографий тренировочного набора;

● test/ — папка, содержащая 224 фотографий для классификации;

● train.csv — содержит в себе 2 столбца id-фотографии и ее класс;

● sample_submission.csv — образец файла для отправки.


Метрика

В качестве метрики выступает Multi AUC-ROC.

Датасет:

kaggle:

https://www.kaggle.com/datasets/dimka11/trash-containers

kaggle datasets download -d dimka11/trash-containers

Model weights:

https://www.kaggle.com/datasets/dimka11/trash-containers-cls-weights

kaggle datasets download -d dimka11/trash-containers-cls-weights


[Мои идеи](https://github.com/dimka11/trash_containers_cls/blob/main/ideas.md)

Финальный результат:  https://github.com/dimka11/trash_containers_final/blob/main/README.md

roc_auc public ~ 0.855

