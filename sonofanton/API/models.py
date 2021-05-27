from django.db import models

class task_data(models.Model):
    task_type = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    deadline = models.CharField(max_length=40)

    def __str__(self):
        return self.task_type

class prompt_data(models.Model):
    gpt_prompt = models.CharField(max_length=150)

    def __str__(self):
        return self.gpt_prompt

class new_text_data(models.Model):
    info_type = models.CharField(max_length=40)
    txt_submit = models.CharField(max_length=100000)

    def __str__(self):
        return self.info_type

class prompt_and_response_data(models.Model):
    text_gen_time = models.DateTimeField()
    the_prompt = models.CharField(max_length=150)
    ai_response = models.CharField(max_length=10000)

    def __str__(self):
        return self.the_prompt
