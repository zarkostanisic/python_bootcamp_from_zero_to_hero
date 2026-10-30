{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "0d2c5b82",
   "metadata": {},
   "source": [
    "Hello World!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "512df003",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello World\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "66220cc7",
   "metadata": {},
   "source": [
    "Test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c1fd4773",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\u001b[1;34musage: \u001b[0m\u001b[1;35mipykernel_launcher.py\u001b[0m [\u001b[32m-h\u001b[0m] [\u001b[32m-v\u001b[0m] [\u001b[32m-q\u001b[0m] [\u001b[36m--locals\u001b[0m] [\u001b[36m--durations \u001b[33mN\u001b[0m] [\u001b[32m-f\u001b[0m]\n",
      "                             [\u001b[32m-c\u001b[0m] [\u001b[32m-b\u001b[0m] [\u001b[32m-k \u001b[33mTESTNAMEPATTERNS\u001b[0m]\n",
      "                             \u001b[32m[tests ...]\u001b[0m\n",
      "ipykernel_launcher.py: \u001b[1;35merror:\u001b[0m \u001b[35margument -f/--failfast: ignored explicit argument 'c:\\\\Users\\\\STANISIC\\\\AppData\\\\Roaming\\\\jupyter\\\\runtime\\\\kernel-v3b1c01ee4b55f1e6815b87f8e4170fc7147fc5557.json'\u001b[0m\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "2",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[31mSystemExit\u001b[39m\u001b[31m:\u001b[39m 2\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\STANISIC\\AppData\\Roaming\\Python\\Python315\\site-packages\\IPython\\core\\interactiveshell.py:3831: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "from unittest import TestCase, main\n",
    "\n",
    "class Evaluate(TestCase):\n",
    "    def test_exercise(self):\n",
    "        self.assertEqual(1, 1, 'Not Equal')\n",
    "        \n",
    "if __name__ == '__main__':\n",
    "    main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.15.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
