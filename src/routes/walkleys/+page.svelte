<script>
  import BackToTop from "$lib/components/BackToTop.svelte";

  // ### Built using this tutorial:
  // https://huggingface.co/docs/transformers.js/en/tutorials/vanilla-js

  import { name } from '$lib/info.js'
  import { onMount } from 'svelte';


// const fileUpload = document.getElementById("file-upload");
// const imageContainer = document.getElementById("image-container");
// const status = document.getElementById("status");

// status.textContent = "Loading model...";
// const detector = await pipeline("object-detection", "Xenova/detr-resnet-50");

  /** @type {import('../tools/$types').PageData} */



</script>

<svelte:head>
  <title>{name}</title>
</svelte:head>

<BackToTop />
<div class = "max-w-4xl mx-auto">

  <h1
  class="text-center font-bold tracking-tight text-zinc-800 dark:text-zinc-100">
  Jump to section:
</h1>
  <ul class="list-inside text-center">
    <li><a href='#rawdata'>Working with raw data</a></li>
    <li><a href='#processed'>Connecting with processed data</a></li>
    <li><a href='#patterns'>Finding patterns</a></li>
  </ul>

</div>

<!-- #### EXTRACTION  -->

<div class="pt-10 pb-10 container text-center tracking-tight text-zinc-800 dark:text-zinc-100">

<h1 id="rawdata">Working with raw data</h1>

<p>This section is about extracting useful information from raw or unstructured data. </p>

<div  class='section pb-10 pt-5'>
<h2 class="font-bold">Named entity extraction</h2>
<p>Enter some text and it will isolate the people, organisations,locations and other entities.</p>

<iframe
	src="https://joshnicholas-named-entity-extract.hf.space"
	frameborder="0"
	width="100%"
	height="500"
></iframe>



<h2 class="font-bold pt-20">Table extraction</h2>
<p>If you upload a screenshot of a table it will generate a json feed.</p>
<p >I've got a sample table <a style="color:#84cc16" href='/budgetExample.png'>here</a> from the Australian federal budget. The code runs cell by cell so it may take a bit of time (especially on larger tables).</p>


  <iframe
	src="https://joshnicholas-table-extract.hf.space"
	frameborder="0"
	width="100%"
	height="500"
></iframe>


</div>


<hr>

<!-- ### Combining/merging  -->


  <h1 id="processed">Connecting with processed data</h1>
  
  <div  class='section pb-10 pt-5'>
  <h2 class="font-bold">Fuzzy matching</h2>


<p>Enter some text and it will isolate the people, organisations and locations.</p>

<iframe
src="https://joshnicholas-fuzzy-matching.hf.space"
frameborder="0"
width="100%"
height="450"
></iframe>

<h2 class="font-bold pt-20">Query a table</h2>

<p class="text-center tracking-tight text-zinc-800 dark:text-zinc-100">If you upload a CSV of a table below you can then ask questions in natural language.</p>
<p class="pt-5 pb-5 text-center tracking-tight">I've got a sample csv <a style="color:#84cc16" href='/boxscore.csv'>here</a> you can play with. It's a cut down box score from a Boston Celtics game. You could ask questions like "What was the average score for the players" or "How many minutes did Jaylen Brown play?"</p>



  <iframe
	src="https://joshnicholas-table-query.hf.space"
	frameborder="0"
	width="100%"
	height="700px"
></iframe>


</div>

<hr>

<!-- ### Categorisation  -->

<h1 id="patterns">Finding patterns</h1>
  
<div  class='section pb-10 pt-5 max-w-4xl mx-auto text-center tracking-tight text-zinc-800 dark:text-zinc-100'>
<h2 class="font-bold">Classification</h2>


<p class="pb-5" >Let's say you have a thousands of articles that you need to put into categories, or prioritise. You could read through them all, or you could use a model to sort through them for you. We had a similar problem on a project at <a style="color:#84cc16" href='https://www.theguardian.com/australia-news/2023/sep/01/coalition-no-campaigners-spending-four-times-more-on-voice-facebook-ads-than-counterparts'>The Guardian</a> - we had thousands of Google ads that we needed to filter to find the ones about the Voice to Parliament.</p>

<p>We trained a classification algorithms to categorise all the ads as either about The Voice or not. The example below has been trained to categorise news articles by subject. Paste in an article and give it a try.</p>

<iframe
	src="https://joshnicholas-news-categorisation.hf.space"
	frameborder="0"
	width="100%"
	height="750"
></iframe>


</div>

</div>

<style>
  /* a {
    @apply flex items-center gap-2 font-medium text-zinc-700;
  } */


  :global(.dark) a {
    @apply text-zinc-300;
  }

  ul {
  list-style-type: circle;
  font-size: 0.8em;
}

.container {
  margin-top: 10px;
}

.container h1{
  margin-top: 20px;
  margin-bottom: 10px;
  text-align: center;
  font-size: 2em;
}

hr {
  height: 1.5px;
background-color: #656565;
margin-top: 20px;
margin-bottom: 20px;
      }


</style>




