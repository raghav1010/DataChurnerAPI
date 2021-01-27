NOTES which I made as I created the second solution :
1. API deals with resources just like in OOPs model
2. API does not interact with model class.
3. A model class behaves as a helper which has couple of methods and it helps us to extract user objects.
4. Basically a Model is an internal representation of an entity and Resources serve as an external entity.
5. The API clients like a website or a mobile application interact with resources , resources are what they see.
6. A resource is used to map endpoints like the http verbs GET , POST , PUT , etc.

Thus , in this approach I separated the models and resources , creating separate packages for them. This made the working of restapi a lot clear to me and also implemented
the database using SQLAlchemy ORM toolkit which made it easier for query fetching.

SQLAlchemy helped me to map objects to database .
Now each Customer_model bject which has 23 attributes like Customer_Age , Gender , etc can easily be inserted , removed , fetched and updated by object mapping .
