# paracli is a simple Python script that parallelize subprocesses like shell commands.

The script looks for a sample_cli.list file that contains the list of commands you need to execute in parallel.

## Usage

```sh
git clone https://github.com/yanlibert/paracli.git
cd paracli
./paracli.py -k n
```

Where n is the number of processes to launch in parallel.

> n cannot be lower than 1 and higher than the number of cpu available.


