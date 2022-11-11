
# Plum Bank

Service which enables plum bank customers to transfer money to other customers and enables customer to view their passbook and account balance

## API Reference

#### Create Customer

```http
  POST /register/
```
Request Body to be passed as form-data via client(postman for local testing)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | **Required** |
| `age` | `integer` | **Required** |

#### Make Payment (Credit/Debit)

```http
  POST /payment/
```

Request Body to be passed as form-data via client(postman for local testing)


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `account_number`      | `integer` | **Required**.|
| `transaction_type`      | `string` | **Required**.  |
| `peer_account_number`      | `integer` | **Required**. |
| `amount`      | `integer` | **Required**. |

#### Get Remaining Balance of Account number

```http
  GET balance/<int:account_number>
```
Account number to be passed in URL

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `none`      | `na` | **Not Required**.|

#### Get Passbook detail of account number

```http
  GET passbook/<int:account_number>
```
Account number to be passed in URL

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `none`      | `na` | **Not Required**.|

## Github Link
Please find the github link below

https://github.com/kkumar0829/PlumBank


## To run code in local
```bash
  pip install -r requirements.txt
```
```bash
  python manage.py makemigrations
```
```bash
  python manage.py migrate
```
```bash
  python manage.py createsuperuser
```
```bash
  python manage.py runserver
```

## 🚀 About Me
I'm a backend developer, Please find me on below link

https://github.com/kkumar0829


