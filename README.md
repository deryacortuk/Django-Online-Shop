[![https://docs.celeryq.dev/en/latest/_images/celery-banner-small.png](https://camo.githubusercontent.com/1b8eb5f2ea4469e45797421fc9a3732ba4bc24508bee42b5a0794317810b9180/68747470733a2f2f646f63732e63656c657279712e6465762f656e2f6c61746573742f5f696d616765732f63656c6572792d62616e6e65722d736d616c6c2e706e67)](https://camo.githubusercontent.com/1b8eb5f2ea4469e45797421fc9a3732ba4bc24508bee42b5a0794317810b9180/68747470733a2f2f646f63732e63656c657279712e6465762f656e2f6c61746573742f5f696d616765732f63656c6572792d62616e6e65722d736d616c6c2e706e67)

 [![Build status](https://github.com/celery/celery/actions/workflows/python-package.yml/badge.svg)](https://github.com/celery/celery/actions/workflows/python-package.yml) [![coverage](https://camo.githubusercontent.com/295da549199e9fecb8a640e66259578f17a0f83bb412805178ee6fdab19635c5/68747470733a2f2f636f6465636f762e696f2f6769746875622f63656c6572792f63656c6572792f636f7665726167652e7376673f6272616e63683d6d6173746572)](https://codecov.io/github/celery/celery?branch=master) [![BSD License](https://camo.githubusercontent.com/45e396a65095ffcf4e27509d344e2ec4959cc5a3e0f9a53a0852c8af942cf828/68747470733a2f2f696d672e736869656c64732e696f2f707970692f6c2f63656c6572792e737667)  ](https://opensource.org/licenses/BSD-3-Clause)[![Celery can be installed via wheel](https://camo.githubusercontent.com/f2a5d283142689b81e8a419df3f2687a6c2b89f320f904a573c6a7c919c85330/68747470733a2f2f696d672e736869656c64732e696f2f707970692f776865656c2f63656c6572792e737667)  ](https://pypi.org/project/celery/)[![Supported Python versions.](https://camo.githubusercontent.com/c04328dfd1a45621e20620b7b4f350366dbe2978bdc00a7e1cc2a9585603c6b7/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f63656c6572792e737667)  ](https://pypi.org/project/celery/)[![Supported Python implementations.](https://camo.githubusercontent.com/025491e05b8ea45f1fe7b723d2e1d652e73d310693cbdfb96bb2848f094835cb/68747470733a2f2f696d672e736869656c64732e696f2f707970692f696d706c656d656e746174696f6e2f63656c6572792e737667)  ](https://pypi.org/project/celery/)[![Backers on Open Collective](https://camo.githubusercontent.com/93161e9735f3ee3472650360b861a768f824ea806a5be60063acb19e2bcb40ec/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f63656c6572792f6261636b6572732f62616467652e737667)](https://github.com/celery/celery#backers) [![Sponsors on Open Collective](https://camo.githubusercontent.com/96b9276f2324187c9dee1225bcd4b0047b278306ce8c083c3ea521e78ff4c758/68747470733a2f2f6f70656e636f6c6c6563746976652e636f6d2f63656c6572792f73706f6e736f72732f62616467652e737667)](https://github.com/celery/celery#sponsors)

Version: 5.3.0b1 (dawn-chorus)

Web: [https://docs.celeryq.dev/en/stable/index.html](https://docs.celeryq.dev/en/stable/index.html)

Download: [https://pypi.org/project/celery/](https://pypi.org/project/celery/)

Source: [https://github.com/celery/celery/](https://github.com/celery/celery/)

Keywords: task, queue, job, async, rabbitmq, amqp, redis, python, distributed, actors


**Celery** is an asynchronous task queue based on distributed message passing. Task queues are used as a strategy to distribute the workload between threads/machines.

Celery is a simple, flexible, and reliable distributed system to process vast amounts of messages, while providing operations with the tools required to maintain such a system.

Celery has a large and diverse community of users and contributors, you should come join us on IRC or our mailing-list.
To work with Celery, we also need to install RabbitMQ because Celery requires an external solution to send and receive messages. Those solutions are called **message brokers**. Currently, Celery supports RabbitMQ, Redis, and Amazon SQS as message broker solutions.

**When and why should you use RabbitMQ?**

Message queueing allows web servers to respond to requests quickly instead of being forced to perform resource-heavy procedures on the spot that may delay response time. Message queueing is also good when you want to distribute a message to multiple consumers or to balance loads between workers.

The consumer takes a message off the queue and starts processing the PDF. At the same time, the producer is queueing up new messages. The consumer can be on a totally different server than the producer or they can be located on the same server. The request can be created in one programming language and handled in another programming language. The point is, the two applications will only communicate through the messages they are sending to each other, which means the sender and receiver have low coupling.

The easiest way to install Celery is using pip:

```bash
pip install celery
```
To install it on a newer Ubuntu version is very straightforward:

```bash
apt-get install -y erlang
apt-get install rabbitmq-server
```

Then enable and start the RabbitMQ service:

```bash
systemctl enable rabbitmq-server
systemctl start rabbitmq-server
```

Check the status to make sure everything is running smooth:

```bash
systemctl status rabbitmq-server
```

##### Installing RabbitMQ on Mac

Homebrew is the most straightforward option:

```bash
brew install rabbitmq
```
# **Monitoring Celery Workers**

There is a handy web-based tool called  [Flower](http://flower.readthedocs.io/en/latest/index.html)  which can be used for monitoring and administrating Celery clusters, Flower provides detailed statistics of task progress and history, It also shows other task details such as the arguments passed, start time, runtime, and others.
# install Flower
```bash
 pip install flower
 ```

Once installed, you must open a new command line in the project directory and run this command :

```bash
 celery -A djangocelery worker -l info 
 ```

then open a  **new command line**  in project path and run this command :
```bash
 celery -A djangocelery flower
 ```
 
Braintree provides an API that allows you to process online payments with multiple payment methods, such as credit card, PayPal, Google Pay, and Apple Pay. 
You can learn more about Braintree at https://www.braintreepayments.com/. Braintree provides different integration options. The simplest is the Drop-in integration, which contains a preformatted payment form. However, in order to customize the behavior and experience of your checkout, you are going to use the advanced Hosted Fields integration. You can learn more about this integration at https://developers.braintreepayments.com/guides/hosted-fields/ overview/javascript/v3The Hosted Fields integration allows you to create your own payment form using custom styles and layouts. An iframe is added dynamically to the page using the Braintree JavaScript software development kit (SDK). The iframe includes the Hosted Fields payment form. When the customer submits the form, Hosted Fields collects the card details securely and attempts to tokenize them. If tokenization succeeds, you can send the generated token nonce to your view to make a transaction using the Python braintree module. A token nonce is a secure, one-time-use reference to payment information. It allows you to send sensitive payment information to Braintree without touching the raw data.

 **Installing the Braintree**
```bash
pip install django-braintree
```
## The Awesome Document Factory

WeasyPrint is a smart solution helping web developers to create PDF documents. It turns simple HTML pages into gorgeous statistical reports, invoices, tickets…

From a technical point of view, WeasyPrint is a visual rendering engine for HTML and CSS that can export to PDF. It aims to support web standards for printing. WeasyPrint is free software made available under a BSD license.

It is based on various libraries but  _not_  on a full rendering engine like WebKit or Gecko. The CSS layout engine is written in Python, designed for pagination, and meant to be easy to hack on.
Install and update using  [pip](https://pip.pypa.io/en/stable/quickstart):

```
pip install weasyprint
```
