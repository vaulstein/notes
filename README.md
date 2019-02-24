## tnote

[![GitHub license](https://img.shields.io/pypi/l/pyzipcode-cli.svg)](https://img.shields.io/pypi/l/pyzipcode-cli.svg) [![Supported python versions](https://img.shields.io/pypi/pyversions/Django.svg)]([![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)]()) [![Join the chat at https://gitter.im/prodicus/tnote](https://badges.gitter.im/prodicus/tnote.svg)](https://gitter.im/prodicus/tnote?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

```
  _   _       _
 | \ | |     | |
 |  \| | ___ | |_ ___  ___
 | . ` |/ _ \| __/ _ \/ __|
 | |\  | (_) | ||  __/\__ \
 |_| \_|\___/ \__\___||___/
```

A dead simple command line note taking app built for you!

## Acknowledgment

Inspired by [tnote](https://github.com/tasdikrahman/tnote) created by tasdikrahman.
Original repo has some bugs, which have been solved in pull requests.
However, the author is not responding, so I created my own version of the repo with changes I thought was required.

This notes module supports multi-line support for Content field.

## Index

- [Demo](#demo)
- [Features](#features)
- [Installation](#installation)
  - [Installing dependencies](#installing-dependencies)
  - [Clone it](#clone-it)
  - [Run it](#run-it)
- [Supported platforms](#supported-platforms)
- [Contributing](#contributing)
  - [To-do](#to-do)
  - [Contributers](#contributers)
- [Issues](#issues)
- [License](#license)
- [Donation](#donation)

## Demo
[:arrow_up: Back to top](#index)

Watch a live demo of it working here

# TODO

***

## Features
[:arrow_up: Back to top](#index)

- **Dead simple to use**: Even your granny would be able to use it. No seriously!
- **Feature rich** Add your precious note with it's _title_ , _content_ , _tags_
- **Secure**: Encrypts your database using standard **AES-256 in CBC mode**. So even if anybody gets hand of your database file. He cannot make any sense of it. [A little demo of what I am doing using it](https://github.com/tasdikrahman/tnote/wiki/So-you-say-it-is-encrypted-eh%3F)

**NOTE**
  _This feature is available/tested only on linux based systems. Support for other OS's coming soon!_

- **Text Highlighting is cross platform** - Supports Linux, Windows, MAC for the terminal based highlighting.
- **Searching for notes is hassle free** in `notes`: It supports full text search for notes based on _content_, _tags_
    - The search query if found in the database will be highlighted if found. Looks pleasing to the eyes
- Ability to add and remove tags for each note.
- Adds timestamp for each note which has been added.
- Written in uncomplicated python.

Need I say more?

***

## Installation
[:arrow_up: Back to top](#index)

#### Installing dependencies

**NOTE** 

On **linux** system, install `libsqlcipher-dev` 

```sh
$ sudo apt-get install libsqlcipher-dev
```

On **Mac OS** systems, you can install it by 

```sh
$ brew install sqlcipher
```

#### Clone it


```sh
$ git clone https://github.com/vaulstein/notes
$ cd notes && pip install -r requirements.txt
```

*Add a symbolic link to it*

```sh
$ chmod +x tnote
$ cd ~/bin/ 
$ ln -s ~/some/path/to/notes
```

Replace `~/some/path/to/notes` by the path where you have cloned the repo. For example if you have cloned it to `~/Downloads/notes` folder than your command should look something like

`$ ln -s ~/Downloads/notes/notes`

#### Run it

Fire it up! :volcano:

`$ notes`

***

## Supported platforms
[:arrow_up: Back to top](#index)

| OS | Support status |
| --- | --- |
| Linux | :white_check_mark: Full support |
| OS X | :white_check_mark: Full support  |
| Windows | :ballot_box_with_check: encrytion of the Database for windows not yet supported |

***

## Contributing
[:arrow_up: Back to top](#index)

This app was created in a timespan of 2 hours while learning to use [peewee (ORM)](https://github.com/coleifer/peewee). So don't be shy to make some PR's here :smile:

#### To-do

  [x] Added support to add multiple content
- [ ] Add **unit tests**. Like real quick!
- [ ] Make it pip installable
- [ ] Ability to edit the content of a note
- [x] Add python2 support
- [x] Add tags support for notes
- [x] Remove tags for notes
- [x] Add option to add title for notes
- [ ] Add option to remove title for notes
- [x] Add option to search for notes using content
- [x] Add option to search for notes using tags
- [ ] Add option to search for notes using title
- [ ] Add option to search for notes using timestamp
- [x] Encrypt the `.db` file using **Sqlcipher**
- [x] Add colorized text to the notes for improved UI
- [ ] Add better UI using **urwid**



## Motivation
[:arrow_up: Back to top](#index)

Why not! Cheers to a crazy weekend :smile:

***

## Issues
[:arrow_up: Back to top](#index)

You can report the bugs at the [issue tracker](https://github.com/vaulstein/notes/issues)

**OR**

You can [tweet me](https://twitter.com/VaulsteinR) if you can't get it to work. In fact, you should tweet me anyway.

***

## License
[:arrow_up: Back to top](#index)


You can find a copy of the License at http://prodicus.mit-license.org/

## Donation
[:arrow_up: Back to top](#index)

Donate to the original developer!

| PayPal | <a href="https://paypal.me/tasdik" target="_blank"><img src="https://www.paypalobjects.com/webstatic/mktg/logo/AM_mc_vs_dc_ae.jpg" alt="Donate via PayPal!" title="Donate via PayPal!" /></a> |
|:-------------------------------------------:|:-------------------------------------------------------------:|
| Gratipay  | <a href="https://gratipay.com/tasdikrahman/" target="_blank"><img src="https://cdn.rawgit.com/gratipay/gratipay-badge/2.3.0/dist/gratipay.png" alt="Support via Gratipay" title="Support via Gratipay" /></a> |
| Patreon | <a href="https://www.patreon.com/tasdikrahman" target="_blank"><img src="http://i.imgur.com/ICWPFOs.png" alt="Support me on Patreon" title="Support me on Patreon" /></a> |
| £ (GBP) | <a href="https://transferwise.com/pay/d804d854-6862-4127-afdd-4687d64cbd28" target="_blank"><img src="http://i.imgur.com/ARJfowA.png" alt="Donate via TransferWise!" title="Donate via TransferWise!" /></a> |
| € Euros | <a href="https://transferwise.com/pay/64c586e3-ec99-4be8-af0b-59241f7b9b79" target="_blank"><img src="http://i.imgur.com/ARJfowA.png" alt="Donate via TransferWise!" title="Donate via TransferWise!" /></a> |
| ₹ (INR)  | <a href="https://www.instamojo.com/@tasdikrahman" target="_blank"><img src="https://www.soldermall.com/images/pic-online-payment.jpg" alt="Donate via instamojo" title="Donate via instamojo" /></a> |
