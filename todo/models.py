from django.db import models

#           ð»å³ç»é¢ä¸ã«è¡¨ç¤ºãããæå­åãå·¦-å®éã«ä¿å­ããããã¼ã¿
#              ãã¼ã¿ä»åã®ä¾ list.htmlã§item.priorityã®ä¸­èº«
PRIORITY = (('danger','high'),('info','nomal'),('success','low'))

# classã«ãã£ã¦ãã¼ãã«ãä½ããã¨ãã§ãã
#      ð»ä»»æã®åå  ð»ç¶æ¿ãmodelsã®ãªãã¸ã§ã¯ã
class TodoModel(models.Model):
    title = models.CharField(max_length=100)# titleã¯char
    memo = models.TextField() # é·ãã®æç« ã¯text
    # ð»list.htmlãããã°ã°ã£ã¦èª¿ã¹ãã®ããã
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY #é¸æè¢ãï¼ã¤ï¼ã¤æå®ããå ´åchoices 
                # ðº ä¸ã§ä½ãå¿è¦ããã
    )
    duedate = models.DateField() #ï¼ï¼ã«ä½ãå¥ããªãã¦ãä½¿ç¨ãããã¨ãã§ãã
    # ð»ãªãã¸ã§ã¯ããæå­åã¨ãã¦è¿ããããããªããã°ã¿ã¤ãã«ã«ãªãã¸ã§ã¯ãåãè¡¨ç¤ºããã
    def __str__(self):
        return self.title