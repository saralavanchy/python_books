#Books system
This project was created with the only objective of learn python. The technologies used on this project are:

- [Language] [Python](https://www.python.org/)
- [Data Model] [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Rest API Framework] [FastAPI](https://fastapi.tiangolo.com/)
- [Graphql Framework] [Strawberry](https://strawberry.rocks/docs)

#### Running the project

To run this project you just need to:

1. Clone project
2. Open it with your IDE of preference
3. Install the dependencies (you will find them on the requirements.tx file)
4. Run the app/main.py file

## GraphQL

The graphql app is available on the /schema endpoint. The availables queries are:

### Queries

example:

```
{
  users {
    name,
    surname,
    email,
    address,
    dni,
    id
  }
}
```

### Mutations

example:

```
mutation {
    addUser(address:"some address", dni: 36734923, email:"some@email.com", name:"jose", surname:"josefo"){ name, surname, email, address, dni, id}

    updateUser(address:"an address 123", id: 4){ name, surname, email, address, dni, id}

    deleteUser(id:1){ name, surname, email, address, dni, id}
}
```

- **addUser**: It add a new user to the users list and return the added user. All the parameters are requited except the dni
- **updateUser**: It change the given values on the user of the given id. The only required parameter is the id. If do not exists an user with the given id it will raise an exception
- **deleteUser**: It delete an user of the users list. If do not exists an user with the given id it will raise an exception
