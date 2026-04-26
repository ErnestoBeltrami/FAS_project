# RISC-V Assembly Analyzer

A tool to analyze compiled C code at assembly level to extract metrics.

## Overview

This project was developed for the *Fundamentals of System Administration* course at UniTrento.

The goal is to provide a clear and practical way to understand how compilers translate high-level C code into RISC-V assembly, and how different optimization levels change the generated instructions.

The tool takes a C source file as input, compiles it into RISC-V assembly (chosen for educational purposes), and performs static analysis to extract useful metrics such as:

- instruction distribution
- most frequently used instruction types
- stack pointer evolution
- register usage patterns

The results are visualized through graphs using Jupyter Notebook.

While primarily designed for educational purposes, this kind of analysis reflects concepts that are particularly relevant in low-level and resource-constrained environments (e.g. embedded systems), where understanding instruction patterns, memory access, and stack usage can help reason about performance and efficiency.

## Example Output

*The upper graph is always related to the non-optimized output while the bottom one has -O2 optimization*

- **Instructions by usage** 
![Instruction Distribution](instruction_distribution.png)

- **Stack-Pointer evolution**
![Stack Pointer](stack_pointer.png)

- **Instruction Category Distribution
![Categories](categories.png)

- **Destination/Source frequency of registers** *(how many times each register was a source or destination in instructions)*
![Registers](registers.png)


### Technologies Used
- Python
- RISC-V compiler
- Docker
- Make
- Jupyter Notebook

### Usage

1. **Build the Docker image**

```bash
sudo make build FILE=path/to/file.c
```

This copies the input C file into the project and builds the Docker image.

---

2. **Start the container**

```bash
sudo docker run --rm -it -p 8888:8888 fas bash
```
- `-it` → interactive shell
- `--rm` → removes container after exit
- `-p 8888:8888` → exposes Jupyter Notebook

---

3. **Run the pipeline**

```bash
make all
```
This will:

- compile the C file with `-O0` and `-O2`
- generate assembly files
- prepare data for analysis

---

4. **Launch Jupyter Notebook**
```bash
make notebook
```

Then open in your browser: http://localhost:8888

### Project Structure

``` 
project/  
│  
├── src/ 
│ ├── parser.py # Parses assembly into structured instructions  
│ ├── analyzer.py # Performs static analysis (stack, registers, etc.)  
│ ├── plots.py # Graph generation using matplotlib  
│  
├── output/ 
│ └── notebook.ipynb  
│  
├── temp/ # Temporary files (assembly, intermediate data)  
│  
├── Makefile # Pipeline automation  
├── Dockerfile # Containerized environment  
├── requirements.txt # Python dependencies  
├── README.md
```
