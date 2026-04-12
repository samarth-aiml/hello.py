{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM8o6sWf4d+yhFNjxOMZAk8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/samarth-aiml/hello.py/blob/main/day-02/project.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name = \"ball\"\n",
        "age = 5\n",
        "price = 30.99\n",
        "print(type(name))\n",
        "print(type(price))\n",
        "print(type(age))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "prpiuEFkA8WJ",
        "outputId": "67649f7c-1b84-4e49-a10e-c9b340ec5313"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'str'>\n",
            "<class 'float'>\n",
            "<class 'int'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"sammarth is me.\",\"cat cst\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a9iIajhWB5NM",
        "outputId": "e6f81a6b-debf-4a72-8884-0fe40bf6d223"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "sammarth is me. cat cst\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(29)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TCPCwVp1CetS",
        "outputId": "1da3b748-1dbd-421d-c879-fce3fb79b441"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "29\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name = \"samarth\"\n",
        "print(name)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "w8mLFq-QGzzL",
        "outputId": "8e4fd6ca-d5b4-4a34-9057-8658d1e5d426"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "samarth\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "age = 45\n",
        "print(\"my age is :\", age)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Sn8HYln9H1Ww",
        "outputId": "cbb3e036-0104-430f-ddb1-c6af7eed4ef2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "my age is : 45\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name = \"lokesh\"\n",
        "print(\"my name is :\",name)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e6ijnOQMIOnG",
        "outputId": "d442a755-42a1-4bef-9149-07749ca57a8c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "my name is : lokesh\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "age = 29\n",
        "old = True\n",
        "name = \"cat\"\n",
        "c = None\n",
        "print(type(age))\n",
        "print(type(old))\n",
        "print(type(name))\n",
        "print(type(c))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jjCU7erlJ9ic",
        "outputId": "aeeb62fd-17cb-4bd0-a324-e79004ac006f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'int'>\n",
            "<class 'bool'>\n",
            "<class 'str'>\n",
            "<class 'NoneType'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name = \"samarth\"\n",
        "studio = \"parala\"\n",
        "client = \"openai\"\n",
        "rating = 4.5\n",
        "project = True\n",
        "price = 789\n",
        "print(type(name))\n",
        "print(type(studio))\n",
        "print(type(client))\n",
        "print(type(rating))\n",
        "print(type(project))\n",
        "print(type(price))\n",
        "print(name)\n",
        "print(studio)\n",
        "print(client)\n",
        "print(rating)\n",
        "print(price)\n",
        "print(project)"
      ],
      "metadata": {
        "id": "FzB1Uof-L9wb",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f76dbfdf-3a68-4f08-99a8-a7a41da2c81e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'str'>\n",
            "<class 'str'>\n",
            "<class 'str'>\n",
            "<class 'float'>\n",
            "<class 'bool'>\n",
            "<class 'int'>\n",
            "samarth\n",
            "parala\n",
            "openai\n",
            "4.5\n",
            "789\n",
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = 56\n",
        "b = 96\n",
        "sum = a+b\n",
        "print(sum)"
      ],
      "metadata": {
        "id": "I52HNQ8BL-RQ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a3c127a3-5bf7-41ef-a15f-3b0cffd0c100"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "152\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#code snippet\n",
        "a = 10241520\n",
        "b = 40051541\n",
        "sum = a+b\n",
        "print(sum)\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "fNQvj5geL-ew",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "39ec07fd-9269-4b5e-f2b2-67d2f4379638"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "50293061\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = 3\n",
        "b = 6\n",
        "sum = a+b\n",
        "print(sum)"
      ],
      "metadata": {
        "id": "yVFx0oe-L-qo",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e7fbb746-8630-46ed-e545-b30f4db75378"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = 34\n",
        "b = 64\n",
        "sum = a*b\n",
        "print(sum)"
      ],
      "metadata": {
        "id": "9o27lxCoL_1w",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0aec78b8-3304-4010-80ac-f5aa245c46bb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2176\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#other operators\n",
        "A = 67\n",
        "B = 89\n",
        "print(A!=B)\n",
        "print(A==B)"
      ],
      "metadata": {
        "id": "KNCJjDwzMAlP",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c8253589-aa87-45c6-9feb-e14a3af6d2e4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n",
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#strings\n",
        "\n",
        "str1 = \"gooogle\"\n",
        "str2 = \"hello\"\n",
        "str3 = \"koogle\"\n",
        "print(str1)"
      ],
      "metadata": {
        "id": "cIfBbcpUMBSg",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2c4d9c49-f33e-46de-a4b2-3a0fb5fefb10"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "gooogle\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "str5 = \"apna college.\\n                                                                                     is good\"\n",
        "print(str5)\n",
        "print(str1+str2)\n",
        "print(str3+str2)\n",
        "final_string = str1 + str2\n",
        "print(final_string)\n"
      ],
      "metadata": {
        "id": "UE9IjUnLMBlY",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "cbb60433-91ba-4c49-a3db-f8fe775d98c5"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "apna college.\n",
            "                                                                                     is good\n",
            "goooglehello\n",
            "kooglehello\n",
            "goooglehello\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#hard concept\n",
        "str1 = \"str\"\n"
      ],
      "metadata": {
        "id": "DSnE44pEMCCg",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a3e088c4-c2cf-4040-a200-9c1df218bd61"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "7\n",
            "106\n",
            "12\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "input(\"enter your name:\")\n",
        "print(\"hello there\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2B0tYckP1MDT",
        "outputId": "3a900b0a-dc37-4976-abb7-a5fd647577d4"
      },
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter your name:Samarth\n",
            "hello there\n"
          ]
        }
      ]
    }
  ]
}