# Archive Toolbox

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-1.0-orange)

## Description

**Archive Toolbox** is a utility for managing archives, allowing you to create, extract, and display information about archives.

## Installation

To install the utility, use `pip`:

```sh
pip install archive_toolbox
```

## Usage

### Command Line

After installation, you can use the utility from the command line with the `atb` command.

```sh
atb --extract --filename <archive.type>
```

### Examples

#### Extracting a ZIP Archive

```sh
atb --extract --filename example.zip
```


#### Extracting a TAR Archive

```sh
atb --extract --filename example.tar
```

#### Extracting a TAR.GZ Archive

```sh
atb --extract --filename example.tar.gz
```
#### Info about a ZIP Archive

```sh
atb --info --filename example.zip
```

#### Info about a TAR Archive

```sh
atb --info --filename example.tar
```

## Features

- **Extract archives**
- **Display information about archive contents**

## Requirements

- Python 3.6 or higher

## License

This project is licensed under the **MIT License**.

## Authors

- **Dementev Maksim** - *Lead Developer* - [Github profile](https://github.com/idmaksim)


