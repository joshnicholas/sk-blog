<script>
  import { name } from '$lib/info.js'
  import { onMount } from 'svelte';
  import Table from '$lib/components/table.svelte'

let datah = []
let groups = []
let colours

  /** @type {import('./$types').PageData} */

  	/** @type {import('./$types').PageData} */
	export let data;
console.log("data: ", data.item)


</script>

<svelte:head>
  <title>{name}</title>
</svelte:head>

  <!-- <p class="pb-5 text-center font-bold tracking-tight" style="color:blue">Have added Brisbane.</p> -->


<div class="container flex flex-col flex-grow grid grid-cols-1 md:grid-cols-2 max-w-4xl mx-auto">

<Table thingo={"Gnews"} standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'Google News'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/google_top/latest.json'}/>

<Table thingo={"Gtrends"}  standfirst={""} removeCol={"Search"} keys={["Search","Rank"]} title = {'Google searches'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/google/latest.json'}/>


<Table thingo={"ABC"} standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'ABC'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/abc_top/latest.json'}/>


<!-- <Table thingo={"SBS"}  standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'SBS top stories'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/sbs_top/latest.json'}/> -->


<Table thingo={"Graun"} standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'Guardian Australia'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/graun_top/latest.json'}/>

<Table thingo={"SMH"} standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'SMH'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/smh_top/latest.json'}/>

<Table thingo={"Age"} standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'The Age'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/age/latest.json'}/>

<Table thingo={"Brisbane"} standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'Brisbane Times'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/brisbane_times/latest.json'}/>


<Table thingo={"News"} standfirst={""} removeCol={"Headline"} keys = {["Headline","Rank"]} title = {'News.com.au'} urlo = {'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/newscom_top/latest.json'}/>


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



