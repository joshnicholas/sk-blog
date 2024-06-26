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

  <!-- <p class="pb-5 text-center font-bold tracking-tight" style="color:red">This page is still under construction. Some of the models/examples need to be added to, cleaned up, swapped out or retrained.</p> -->

  <h1
  class="pb-5 text-center font-bold tracking-tight">
  Jump to section:
</h1>
  <ul class="list-inside text-center">
    <li><a href='#rawdata'>Extracting info from text</a></li>
    <li><a href='#processed'>Making connections between data</a></li>
    <li><a href='#patterns'>Finding a needle in a haystack</a></li>
  </ul>

</div>

<!-- #### EXTRACTION  -->

<div class="pt-10 pb-10 container text-center tracking-tight">

<h1 id="rawdata">Extracting info from text</h1>

<p>Control-F is great if you know exactly what you're trying to find. But what if you know a document contains a bunch of names, locations, or even dollar amounts, but don't know exactly what they are?</p>

<div  class='section pb-10 pt-5'>
<!-- <h2 class="font-bold">Named entity extraction</h2> -->
<p>This process is called named-entity recognition, and the model will identify the names of people, places and things within a text.</p>


<iframe
	src="https://joshnicholas-named-entity-extract.hf.space"
	frameborder="0"
	width="100%"
	height="500"
></iframe>

<p>You can find the code for this on <a class="mt-20" href='https://huggingface.co/spaces/Joshnicholas/named_entity_extract/tree/main'>Huggingface</a> and a notebook version on <a class="mt-10" href='https://github.com/joshnicholas/walkeys-journalism-ai-training'>Github</a></p>

<!-- <h2 class="font-bold pt-20">Table extraction</h2>
<p>If you upload a screenshot of a table it will generate a json feed.</p>
<p >I've got a sample table <a style="color:#84cc16" href='/budgetExample.png'>here</a> from the Australian federal budget. The code runs cell by cell so it may take a bit of time (especially on larger tables).</p>


  <iframe
	src="https://joshnicholas-table-extract.hf.space"
	frameborder="0"
	width="100%"
	height="500"
></iframe> -->


</div>


<hr>

<!-- ### Combining/merging  -->


  <h1 id="processed">Making connections between datasets</h1>
  
  <div  class='section pb-10 pt-5'>
  <!-- <h2 class="font-bold">Fuzzy matching</h2> -->

<p class="pb-5">Let's say you have a bunch of locations from <a href='https://www.theguardian.com/australia-news/ng-interactive/2022/may/17/pork-barrel-spending-australia-politics-barrelling-figures-money-australian-federal-election-2022-tracking-projects-promises-announcements-by-electorate-anthony-albanese-scott-morrison-campaign-visit-map'>government election promises</a> and need to find where these places are in reality. Or you might have a trove of documents and want to group them together by theme. This kind of "matching" problem is really common in investigative journalism.</p>
<p>This tool will take two lists of names that are similar - but not quite the same - and match them together.</p>

<iframe
src="https://joshnicholas-fuzzy-matching.hf.space"
frameborder="0"
width="100%"
height="450"
></iframe>

<p>You can find the code for this on <a class="mt-20"  href='https://huggingface.co/spaces/Joshnicholas/fuzzy-matching/tree/main'>Huggingface</a> and a notebook version on <a class="mt-10"  href='https://github.com/joshnicholas/walkeys-journalism-ai-training'>Github</a></p>


<!-- <h2 class="font-bold pt-20">Query a table</h2>

<p class="text-center tracking-tight text-zinc-800 dark:text-zinc-100">If you upload a CSV of a table below you can then ask questions in natural language.</p>
<p class="pt-5 pb-5 text-center tracking-tight">I've got a sample csv <a style="color:#84cc16" href='/boxscore.csv'>here</a> you can play with. It's a cut down box score from a Boston Celtics game. You could ask questions like "What was the average score for the players" or "How many minutes did Jaylen Brown play?"</p>



  <iframe
	src="https://joshnicholas-table-query.hf.space"
	frameborder="0"
	width="100%"
	height="700px"
></iframe> -->


</div>

<hr>

<!-- ### Categorisation  -->

<h1 id="patterns">Finding a needle in a haystack</h1>
  
<div  class='section pb-10 pt-5 max-w-4xl mx-auto text-center tracking-tight'>
<!-- <h2 class="font-bold">Classification</h2> -->


<p class="pb-5" >Let's say you have thousands of images and you need to identify something in them. You could look through them all, or you could use a model to sort through them for you. We had a similar problem on a project at <a  href='https://www.theguardian.com/news/datablog/2022/may/19/reality-cheque-we-taught-ai-artificial-intelligence-to-spot-the-most-used-props-australian-federal-election-2022'>The Guardian</a> - we had loads of photos from the election campaign and wanted to find hi-vis vests.</p>

<p>We trained a classification algorithms to find what we wanted. But the following example uses an OpenAI model to predict what its an image without fine-tuning.</p>

<!-- <iframe
	src="https://joshnicholas-news-categorisation.hf.space"
	frameborder="0"
	width="100%"
	height="750"
></iframe> -->

<iframe
	src="https://joshnicholas-image-classifier.hf.space"
	frameborder="0"
	width="100%"
	height="1200px"
></iframe>


<p>You can find the code for this on <a class="mt-20"  href='https://huggingface.co/spaces/Joshnicholas/news_categorisation/tree/main'>Huggingface</a> and a notebook version on <a class="mt-10" href='https://github.com/joshnicholas/walkeys-journalism-ai-training'>Github</a></p>

</div>

</div>

<style>
  /* a {
    @apply flex items-center gap-2 font-medium text-zinc-700;
  } */



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
/* background-color: #656565; */
margin-top: 20px;
margin-bottom: 20px;
      }


</style>




