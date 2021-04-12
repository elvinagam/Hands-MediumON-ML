# ML
There is generally different ways to both train and server models into production:

### Train: one off, batch and real-time/online training
### Serve: Batch, Realtime (Database Trigger, Pub/Sub, web-service, inApp)

## Model Format

Pickle converts a python object to to a bitstream and allows it to be stored to disk and reloaded at a later time. It is provides a good format to store machine learning models provided that their intended applications is also built in python.

ONNX the Open Neural Network Exchange format, is an open format that supports the storing and porting of predictive model across libraries and languages. Most deep learning libraries support it and sklearn also has a library extension to convert their model to ONNX’s format.

PMML or Predictive model markup language, is another interchange format for predictive models. Like for ONNX sklearn also has another library extension for converting the models to PMML format. It has the drawback however of only supporting certain type of prediction models.PMML has been around since 1997 and so has a large footprint of applications leveraging the format. Applications such as SAP for instance is able to leverage certain versions of the PMML standard, likewise for CRM applications such as PEGA.

POJO and MOJO are H2O.ai’s export format, that intendeds to offers an easily embeddable model into java application. They are however very specific to using the H2O’s platform.

