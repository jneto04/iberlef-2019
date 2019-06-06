# Task 1 - Named Entity Recognation

The first task we propose is NER, the task of identifying proper nouns within a given text and classifying them into one of many relevant categories or within a default category known as Miscellaneous. Our objective with this task is to evaluate the proposed systems in many textual genres. For datasets that have as main textual genres: news, memorandums, e-mails, interviews and magazine articles, we will evaluate the following categories: PER – Person, PLC – Place, ORG – Organization, VAL – Value and TME – Time. On the other hand, for Clinical notes and Legal texts, of which we will only evaluate the PER – Person category.

<table class="tg">
  <tr>
    <th class="tg-7btt">Participante</th>
    <th class="tg-7btt">Corpus</th>
    <th class="tg-7btt">Categoria</th>
    <th class="tg-7btt">Prec</th>
    <th class="tg-7btt">Rec</th>
    <th class="tg-7btt">F1</th>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="8">Pedro Vitor</td>
    <td class="tg-c3ow">Policia</td>
    <td class="tg-c3ow">PER</td>
    <td class="tg-c3ow">86.14%</td>
    <td class="tg-c3ow">92.82%</td>
    <td class="tg-c3ow">89.35%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Evoluções</td>
    <td class="tg-c3ow">PER</td>
    <td class="tg-c3ow">32.47%</td>
    <td class="tg-c3ow">51.02%</td>
    <td class="tg-c3ow">39.68%</td>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="6">SIGARRA + SecHAREM</td>
    <td class="tg-c3ow">Overall</td>
    <td class="tg-c3ow">63.11%</td>
    <td class="tg-c3ow">51.69%</td>
    <td class="tg-c3ow">56.83%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">ORG</td>
    <td class="tg-c3ow">57.90%</td>
    <td class="tg-c3ow">31.26%</td>
    <td class="tg-c3ow">40.60%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">PER</td>
    <td class="tg-c3ow">83.93%</td>
    <td class="tg-c3ow">77.17%</td>
    <td class="tg-c3ow">80.41%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">PLC</td>
    <td class="tg-c3ow">54.61%</td>
    <td class="tg-c3ow">55.59%</td>
    <td class="tg-c3ow">55.10%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">TME</td>
    <td class="tg-c3ow">59.49%</td>
    <td class="tg-c3ow">57.10%</td>
    <td class="tg-c3ow">58.27%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">VAL</td>
    <td class="tg-c3ow">11.32%</td>
    <td class="tg-c3ow">80.00%</td>
    <td class="tg-c3ow">19.83%</td>
  </tr>
</table>

<table class="tg">
  <tr>
    <th class="tg-7btt">Participante</th>
    <th class="tg-7btt">Corpus</th>
    <th class="tg-7btt">Categoria</th>
    <th class="tg-7btt">Prec</th>
    <th class="tg-7btt">Rec</th>
    <th class="tg-7btt">F1</th>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="8">Juliana</td>
    <td class="tg-c3ow">Policia</td>
    <td class="tg-c3ow">PER</td>
    <td class="tg-c3ow">29.59%</td>
    <td class="tg-c3ow">58.41%</td>
    <td class="tg-c3ow">39.28%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Evoluções</td>
    <td class="tg-c3ow">PER</td>
    <td class="tg-c3ow"> 14.29%</td>
    <td class="tg-c3ow">10.09%</td>
    <td class="tg-c3ow">11.83%</td>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="6">SIGARRA + SecHAREM</td>
    <td class="tg-c3ow">Overall</td>
    <td class="tg-c3ow">56.26%</td>
    <td class="tg-c3ow"> 49.26%</td>
    <td class="tg-c3ow">52.53%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">ORG</td>
    <td class="tg-c3ow">42.27%</td>
    <td class="tg-c3ow">31.77%</td>
    <td class="tg-c3ow">36.28%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">PER</td>
    <td class="tg-c3ow">57.39%</td>
    <td class="tg-c3ow">60.62%</td>
    <td class="tg-c3ow">58.96%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">PLC</td>
    <td class="tg-c3ow">37.35%</td>
    <td class="tg-c3ow">49.34%</td>
    <td class="tg-c3ow">42.52%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">TME</td>
    <td class="tg-c3ow">71.33%</td>
    <td class="tg-c3ow">73.68%</td>
    <td class="tg-c3ow">72.48%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">VAL</td>
    <td class="tg-c3ow">80.19%</td>
    <td class="tg-c3ow">6.14%</td>
    <td class="tg-c3ow">11.40%</td>
  </tr>
</table>

<table class="tg">
  <tr>
    <th class="tg-7btt">Participante</th>
    <th class="tg-7btt">Corpus</th>
    <th class="tg-7btt">Categoria</th>
    <th class="tg-7btt">Prec</th>
    <th class="tg-7btt">Rec</th>
    <th class="tg-7btt">F1</th>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="8">João</td>
    <td class="tg-c3ow">Policia</td>
    <td class="tg-c3ow">PER</td>
    <td class="tg-c3ow">21.72%</td>
    <td class="tg-c3ow">53.07%</td>
    <td class="tg-c3ow">30.83%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Evoluções</td>
    <td class="tg-c3ow">PER</td>
    <td class="tg-c3ow">27.27%</td>
    <td class="tg-c3ow">26.25%</td>
    <td class="tg-c3ow">26.75%</td>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="6">SIGARRA + SecHAREM</td>
    <td class="tg-c3ow">Overall</td>
    <td class="tg-c3ow">26.08%</td>
    <td class="tg-c3ow">19.78%</td>
    <td class="tg-c3ow">22.50%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">ORG</td>
    <td class="tg-c3ow">19.41%</td>
    <td class="tg-c3ow">12.62%</td>
    <td class="tg-c3ow">15.30%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">PER</td>
    <td class="tg-c3ow">50.07%</td>
    <td class="tg-c3ow">34.34%</td>
    <td class="tg-c3ow">40.74%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">PLC</td>
    <td class="tg-c3ow">42.31%</td>
    <td class="tg-c3ow">20.64%</td>
    <td class="tg-c3ow">27.75%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">TME</td>
    <td class="tg-c3ow">8.99%</td>
    <td class="tg-c3ow">11.11%</td>
    <td class="tg-c3ow">9.94%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">VAL</td>
    <td class="tg-c3ow">56.60%</td>
    <td class="tg-c3ow">54.55%</td>
    <td class="tg-c3ow">55.56%</td>
  </tr>
</table>

<table class="tg">
  <tr>
    <th class="tg-7btt">Participante</th>
    <th class="tg-7btt">Corpus</th>
    <th class="tg-7btt">Categoria</th>
    <th class="tg-7btt">Prec</th>
    <th class="tg-7btt">Rec</th>
    <th class="tg-7btt">F1</th>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="8">Pablo<br>(Embeddings)</td>
    <td class="tg-c3ow">Policia</td>
    <td class="tg-c3ow">PER</td>
    <td class="tg-c3ow">92.20%</td>
    <td class="tg-c3ow">89.73%</td>
    <td class="tg-c3ow">90.95%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Evoluções</td>
    <td class="tg-c3ow">PER</td>
    <td class="tg-c3ow">36.36%</td>
    <td class="tg-c3ow">49.12%</td>
    <td class="tg-c3ow">41.79%</td>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="6">SIGARRA + SecHAREM</td>
    <td class="tg-c3ow">Overall</td>
    <td class="tg-c3ow">61.27%</td>
    <td class="tg-c3ow">46.07%</td>
    <td class="tg-c3ow">52.60%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">ORG</td>
    <td class="tg-c3ow">54.24%</td>
    <td class="tg-c3ow">28.04%</td>
    <td class="tg-c3ow">36.97%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">PER</td>
    <td class="tg-c3ow">75.64%</td>
    <td class="tg-c3ow">58.83%</td>
    <td class="tg-c3ow">66.18%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">PLC</td>
    <td class="tg-c3ow">55.93%</td>
    <td class="tg-c3ow">42.47%</td>
    <td class="tg-c3ow">48.28%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">TME</td>
    <td class="tg-c3ow">58.68%</td>
    <td class="tg-c3ow">58.57%</td>
    <td class="tg-c3ow">58.62%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">VAL</td>
    <td class="tg-c3ow">96.23%</td>
    <td class="tg-c3ow">96.23%</td>
    <td class="tg-c3ow">96.23%</td>
  </tr>
</table>

<table class="tg">
  <tr>
    <th class="tg-7btt">Participante</th>
    <th class="tg-7btt">Corpus</th>
    <th class="tg-7btt">Categoria</th>
    <th class="tg-7btt">Prec</th>
    <th class="tg-7btt">Rec</th>
    <th class="tg-7btt">F1</th>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="8">Pablo (LK)</td>
    <td class="tg-c3ow">Policia</td>
    <td class="tg-c3ow">PER</td>
    <td class="tg-c3ow">40.83%</td>
    <td class="tg-c3ow">25.92%</td>
    <td class="tg-c3ow">31.71%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Evoluções</td>
    <td class="tg-c3ow">PER</td>
    <td class="tg-c3ow">22.08%</td>
    <td class="tg-c3ow">6.88%</td>
    <td class="tg-c3ow">10.49%</td>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="6">SIGARRA + SecHAREM</td>
    <td class="tg-c3ow">Overall</td>
    <td class="tg-c3ow">44.89%</td>
    <td class="tg-c3ow">32.97%</td>
    <td class="tg-c3ow">38.01%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">ORG</td>
    <td class="tg-c3ow">38.40%</td>
    <td class="tg-c3ow">19.99%</td>
    <td class="tg-c3ow">26.29%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">PER</td>
    <td class="tg-c3ow">56.79%</td>
    <td class="tg-c3ow">27.59%</td>
    <td class="tg-c3ow">37.14%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">PLC</td>
    <td class="tg-c3ow">39.61%</td>
    <td class="tg-c3ow">23.09%</td>
    <td class="tg-c3ow">29.17%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">TME</td>
    <td class="tg-c3ow">44.59%</td>
    <td class="tg-c3ow">89.79%</td>
    <td class="tg-c3ow">59.59%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">VAL</td>
    <td class="tg-c3ow">34.91%</td>
    <td class="tg-c3ow">42.05%</td>
    <td class="tg-c3ow">38.14%</td>
  </tr>
</table>

<table class="tg">
  <tr>
    <th class="tg-7btt">Participante</th>
    <th class="tg-7btt">Corpus</th>
    <th class="tg-7btt">Categoria</th>
    <th class="tg-7btt">Prec</th>
    <th class="tg-7btt">Rec</th>
    <th class="tg-7btt">F1</th>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="8">Joaquim</td>
    <td class="tg-c3ow">Policia</td>
    <td class="tg-c3ow">PER</td>
    <td class="tg-c3ow">94.21%</td>
    <td class="tg-c3ow">82.82%</td>
    <td class="tg-c3ow">88.15%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Evoluções</td>
    <td class="tg-c3ow">PER</td>
    <td class="tg-c3ow">22.08%</td>
    <td class="tg-c3ow">41.46%</td>
    <td class="tg-c3ow">28.81%</td>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="6">SIGARRA + SecHAREM</td>
    <td class="tg-c3ow">Overall</td>
    <td class="tg-c3ow">75.28%</td>
    <td class="tg-c3ow">59.82%</td>
    <td class="tg-c3ow">66.66%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">ORG</td>
    <td class="tg-c3ow">65.13%</td>
    <td class="tg-c3ow">35.32%</td>
    <td class="tg-c3ow">45.80%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">PER</td>
    <td class="tg-c3ow">65.96%</td>
    <td class="tg-c3ow">54.33%</td>
    <td class="tg-c3ow">59.58%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">PLC</td>
    <td class="tg-c3ow">55.81%</td>
    <td class="tg-c3ow">61.40%</td>
    <td class="tg-c3ow">58.47%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">TME</td>
    <td class="tg-c3ow">94.43%</td>
    <td class="tg-c3ow">87.44%</td>
    <td class="tg-c3ow">90.80%</td>
  </tr>
  <tr>
    <td class="tg-c3ow">VAL</td>
    <td class="tg-c3ow">88.68%</td>
    <td class="tg-c3ow">87.04%</td>
    <td class="tg-c3ow">87.85%</td>
  </tr>
</table>
