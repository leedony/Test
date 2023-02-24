# pI Calculator Instruction

Isoelectric point (pI) predictor for chemically modified peptides and proteins. Both FASTA and CSV files are allowed.

### Input
A FASTA file contians amino acid sequence
</br>
<img src="https://raw.githubusercontent.com/leedony/Test/main/antibody_FASTA_sample.png" width = "500" height = "250" div/>

**OR**

A organized CSV file contains three columns, including '**ID**', '**VH**', '**VL**'
</br>
![图片](https://raw.githubusercontent.com/leedony/Test/main/antibody_csv_format.png)

Here, IgG antibodies are highly recommended for more accurate prediciton. 
The common **CH** and **CL** are provided as follows,

        CH = 'ASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSL…………**'
        CL = 'RTVAAPSVFIFPPSDEQLKSGTASVVCLLNNFYPREAKVQWKVDNALQSGNSQESVTEQDSKDS…………**'
### Parameters
##### Format
Choose the right format for your sequences
##### Complement
Choose if need the default **CH** and **CL** to complete VH and VL into **IgG** 
### Output
A csv file will be generated after processing and it contains the predicted pI values based on **Sillero** and **Nozaki** methods. Both of them show the results that are close to experimental measurements. This is just good for the initial screening.

### Referenece
The available pka sets employed are:

<div id="refer-anchor-1"></div>

- [1] [Sillero](http://europepmc.org/article/MED/2774179)
<div id="refer-anchor-2"></div>

- [2] [Nozaki](https://www.jbc.org/article/S0021-9258(19)77210-X/fulltext)
