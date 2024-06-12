<script>
  import { name } from '$lib/info.js'
  import { onMount } from 'svelte';
  import Table from '$lib/components/table.svelte'
  import NewTable from '$lib/components/newTable.svelte';
  import TestTable from '$lib/components/testTable.svelte';

let datah = []
let groups = []
let colours


	export let data;
  // console.log("data: ", data)

//   // let keys = new Set([...data.agel.map(d => d.publication)]) 
  let keys = Object.keys(data.agel)

  // console.log("keys: ", keys) 

  // ['smh', 'abc', 'news', 'graun', 'age', 'bris', 'goog_news', 'wiki', 'goog_trends']

  let thingos = {

  "goog_news" : {"remove":"Headline", "standfirst": "", "keys": ["Headline","Rank"], "title": 'Google News' },

"goog_trends": {"remove":"Headline", "standfirst": "", "keys": ["Search","Rank"], "title": 'Google Search trending' },

"abc": {"remove":"Headline", "standfirst": "", "keys": ["Headline","Rank"], "title": 'ABC' },

"graun": {"remove":"Headline", "standfirst": "", "keys": ["Headline","Rank"], "title": 'Guardian Australia' },

"smh": {"remove":"Headline", "standfirst": "", "keys": ["Headline","Rank"], "title": 'Sydney Morning Herald' },

"age": {"remove":"Headline", "standfirst": "", "keys": ["Headline","Rank"], "title": 'The Age' },

"bris": {"remove":"Headline", "standfirst": "", "keys": ["Headline","Rank"], "title": 'Brisbane Times' },

"news": {"remove":"Headline", "standfirst": "", "keys": ["Headline","Rank"], "title": 'News.com.au' },

"wiki": {"remove":"Headline", "standfirst": "This data is only updated once per day. Special Wikipedia pages (search page, main page etc.) have been removed, so some page ranks will be missing. ", "keys": ["Page",'Rank', ], "title": 'Wikipedia' },

  }

// let thingo = "bris"

// console.log(data.agel[thingo])
</script>


<svelte:head>
  <title>{name}</title>
</svelte:head>

  <!-- <p class="pb-5 text-center font-bold tracking-tight" style="color:blue">Have added Brisbane.</p> -->

  <!-- <p class='text-center'>I've paused this page as I migrate the dashboard to a <a href='https://joshnicholas.observablehq.cloud/kurumba/'>new site</a>.</p> -->

  <p class='text-center'>Just trying something new.</p>
<br>
  <p class='text-center'>You can download the latest scraped data
  <a href="/dash.csv" download>here</a>.
  </p>

<div class="container flex flex-col flex-grow grid grid-cols-1 md:grid-cols-2 max-w-4xl mx-auto">

  <!-- <NewTable  thingo={thingos[thingo]} standfirst={thingos[thingo]['standfirst']} 
  removeCol={thingos[thingo]['remove']} keys = {thingos[thingo]['keys']} title = {thingos[thingo]['title']} datah = {data.agel[thingo]}/> -->

{#each Object.keys(thingos) as thingo}

  <NewTable  thingo={thingo} standfirst={thingos[thingo]['standfirst']} 
  removeCol={thingos[thingo]['remove']} keys = {thingos[thingo]['keys']} title = {thingos[thingo]['title']} datah = {data.agel[thingo]}/>


{/each}

 <!-- <Table thingo={"Gnews"} standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'Google News'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/google_top/latest.json'}/> -->
  <!-- <NewTable  thingo={"Age"} standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'The Age'} datah = {data.agel['age']}/> -->



<!-- <Table thingo={"Gtrends"}  standfirst={""} removeCol={"Search"} keys={["Search","Rank"]} title = {'Google searches'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/google/latest.json'}/> -->


<!-- <Table thingo={"ABC"} standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'ABC'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/abc_top/latest.json'}/> -->


<!-- <Table thingo={"SBS"}  standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'SBS top stories'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/sbs_top/latest.json'}/> -->


<!-- <Table thingo={"Graun"} standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'Guardian Australia'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/graun_top/latest.json'}/> -->

<!-- <Table thingo={"SMH"} standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'SMH'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/smh_top/latest.json'}/> -->

<!-- <Table thingo={"Age"} standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'The Age'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/age/latest.json'}, datah = {data.age}/> -->

<!-- <Table thingo={"Brisbane"} standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'Brisbane Times'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/brisbane_times/latest.json'}/> -->


<!-- <Table thingo={"News"} standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'News.com.au'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/newscom_top/latest.json'}/> -->


<!-- <Table thingo={"Techmem"}  standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'Tech Meme top stories'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/tech_meme_top/latest.json'}/> -->



<!-- <Table thingo={"Wiki"}  standfirst={"This data is only updated once per day. Special Wikipedia pages (search page, main page etc.) have been removed, so some page ranks will be missing. "} removeCol={"Page"} keys={["Page",'Rank', ]} title = {'Wikipedia'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/wiki/latest.json'}/> -->




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
</style>



