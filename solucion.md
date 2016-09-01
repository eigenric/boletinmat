##### Ricardo Ruiz Fernández de Alba - 2º Bachiller IES Alborán

#### Determina todos los conjuntos de números naturales consecutivos cuya suma vale 91

Necesitamos hallar todos los subconjuntos de $\mathbb N$ de números consecutivos que sumen 91.

$$
	\{m, m+1, m+2, ..., n \} \subset \mathbb N \\
	\sum_{k=m}^nk = 91
$$
Si pensamos que $$3+4+5= (1+2+3+4+5) - (1+2)$$ podemos expresar este conjunto como una diferencia entre dos *segmentos de sucesión natural.*
$$
\{m, m+1, m+2, \ldots, n\} = |1, n| \setminus |1, m-1|\\
$$
Así pues, la suma será
$$
\sum_{k=m}^nk = \sum_{k=1}^nk- \sum_{k=1}^{m-1}k = 91
$$
Y considerando la conocida fórmula
$$
\sum_{k=1}^nk=\frac{n(n+1)}{2}
$$
que [queda demostrada en el anexo](#anexo), podemos expresar la suma finalmente como

$$
\sum_{k=m}^nk = \sum_{k=1}^nk- \sum_{k=1}^{m-1}k = \\
=\frac{n(n+1)}{2} - \frac{(m-1)(m-1+1)}{2} = \\
=\frac{n(n+1) - m(m-1)}{2} = 91
$$
Como buscamos los $(n,m)\in\mathbb N$ que cumplan esta ecuación, se trataría de una **Ecuación "diofántica" (limitada a $\mathbb N$)** 

Simplificando,
$$
\frac{n(n+1) - m(m-1)}{2} = 91 \\
n(n+1) - m(m-1) = 182 \\
n^2+n-m^2+m = 182 \\
n^2-m^2+n+m = 182 \\
(n+m)(n-m)+(n+m) = 182 \\
$$
Y finalmente sacando factor común nos queda:
$$
(n+m)(n-m+1) = 182
$$
Si consideramos a $182$ como producto de dos factores naturales $b$ y $c$, podemos convertir la ecuación en un **Sistema lineal de dos ecuaciones con dos incógnitas.**
$$
(n+m)(n-m+1) = 182 = bc \\
\left\{ 
\begin{array}{c}
n + m= b \\ 
n-m +1 = c
\end{array}
\right. 
$$
 
Resolviendo el sistema por reducción, se obtiene:
$$
   n = \frac{b+c-1}{2}, m = \frac{b-c+1}{2}
$$
Además, se tiene que cumplir que $n \gt 0$, $m \gt 0$ y que $n \gt m$
$$
n = \frac{b+c-1}{2} \gt 0; b \gt 1-c \\
m = \frac{b-c+1}{2} \gt 0; b \gt c -1 \\
\frac{b+c-1}{2} \gt \frac{b-c+1}{2} \\
2c \gt 2; c \gt 1; c - 1 \gt 0
$$
De tal manera que la condición resumen es
$$
b \gt c -1 \gt 0
$$

Siendo $182 = 2\cdot7\cdot13$,  las parejas de factores que cumplen esta condición son:

$$
\begin{align}
(I) \quad b= 2\cdot7 = 14, c = 13 \\
(II) \quad b = 2\cdot13 = 26, c = 7 \\
(III) \quad b = 7\cdot13 = 91, c= 2
\end{align}
$$

Y los correspondientes $n$ y $m$ serían:
$(I)$
$$
\begin{align}
n=\frac{14+13-1}{2}=13\\
m = \frac{14-13+1}{2} = 1\\
\end{align}
$$
$(II)$
$$
\begin{align}
n = \frac{26+7-1}{2} = 16\\
m = \frac{26-7+1}{2} = 10
\end{align}
$$
$(III)$
\begin{align}
n = \frac{91+2-1}{2} = 46\\
m = \frac{91-2+1}{2} = 45
\end{align}

Como conclusión, los subconjuntos de números consecutivos en $\mathbb N$ que suman $91$ son:

$$
\{1,2,3, \ldots, 13\}\\
\{10, 11, 12, \ldots, 16\}\\
\{45, 46\}
$$

#### Anexo: Demostración de la fórmula {#anexo}
Se va a demostrar por inducción la siguiente proposición.

$$
P(n) = \sum_{k=1}^nk = \frac{n(n+1)}{2} 
$$
1) $P(1)$ es cierta
$$
     1 = \frac{1(1+1)}{2}
$$
2) Suponiendo $P(n)$ cierta, demostramos $P(n+1)$
$$
	\sum_{k=1}^{n+1}k = \frac{(n+1)(n+2)}{2}\\	
	=\frac{(n+1)(n+2)}{2} =\frac{n^2+2n+n+2}{2} = \\
	 =\frac{n^2+n}{2} + \frac{2n+2}{2}= \frac{n(n+1)}{2} + n+1 = \\
	 \text{Y, por hipótesis de inducción,} \\
	 = \left(\sum_{k=1}^nk\right)+(n+1) =
	  \sum_{k=1}^{n+1}k
$$

