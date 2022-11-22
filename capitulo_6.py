{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMHSSl3ixYjEpmLPIpoUyZl",
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
        "<a href=\"https://colab.research.google.com/github/italosilva18/PYTHON/blob/main/capitulo_6.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Hb2NgALc5fDx",
        "outputId": "41569c1c-732e-4e15-8ef6-e080d9d73835"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Media: 7.00\n"
          ]
        }
      ],
      "source": [
        "#PROGRAMA 6.1 - Calcula media \n",
        "notas=[6,7,5,8,9]\n",
        "soma=0\n",
        "x=0\n",
        "while x<5:\n",
        "  soma+= notas[x]\n",
        "  x+=1\n",
        "print(f\"Media:{soma/x:5.2f}\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#PROGRAMA 6.2 - CALCULO DA MEDIA COM NOTAS DIGITADAS\n",
        "notas=[0,0,0,0,0]\n",
        "soma=0\n",
        "x=0\n",
        "while x<5:\n",
        "  notas[x]=float(input(f\"Nota{x}:\"))\n",
        "  soma += notas[x]\n",
        "  x+=1\n",
        "x=0\n",
        "while x<5:\n",
        "  print(f\"Nota{x}:{notas[x]:6.2f}\")\n",
        "  x+=1\n",
        "print(f\"Média:{soma/x:5.2f}\")"
      ],
      "metadata": {
        "id": "iYomm7Sc5pGa"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "***Exercicio*** *6.1*:\n",
        ">Modifique o programa 6.2 para ler 7 notas em vez de 5."
      ],
      "metadata": {
        "id": "h-xWi-MpFNJo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Exercicio 6.1 - CALCULO DA MEDIA COM NOTAS DIGITADAS\n",
        "notas=[0,0,0,0,0,0,0]\n",
        "soma=0\n",
        "x=0\n",
        "while x<7:\n",
        "  notas[x]=float(input(f\"Nota{x}:\"))\n",
        "  soma += notas[x]\n",
        "  x+=1\n",
        "x=0\n",
        "while x<7:\n",
        "  print(f\"Nota{x}:{notas[x]:6.2f}\")\n",
        "  x+=1\n",
        "print(f\"Média:{soma/x:5.2f}\")"
      ],
      "metadata": {
        "id": "PmNW-X_7E8Pv"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#PROGRAMA 6.3 - Apresentação de numeros\n"
      ],
      "metadata": {
        "id": "wnMVS-_oGTbV"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}