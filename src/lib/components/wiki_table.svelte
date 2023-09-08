<script>
  import * as d3 from 'd3';
  import { Styles,Input } from 'sveltestrap';
  import Table from '$lib/components/table.svelte'
    import { parse } from 'date-fns'

	export let title

  export let urlo;
  let tableData =[
			{
				vitae : "dolorem",
				lectus : "ipsum",
				quisquam : "quia"
			},
			{
				vitae : "amet",
				lectus : "consectetur",
				quisquam : "adipisci"
			}
		];

let remove = ['Portal:Current_events', 'Wikipedia', 'Main_Page', 
'Special:Search', 'Special:Random', "Special:Watchlist",'Special:Randompage',
'Special:Book','Special:CreateAccount','Special:RecentChanges','Help:Your first article',
'Portal:Contents','Wikipedia:Contact us','Wikipedia:About','Wikipedia:Contact_us','Wikipedia:Citation_needed',
'Wikipedia:Featured_pictures']

let keep = []
let inter
let keys = ['Rank', "Page"]

const parseTime = d3.timeParse("%Y_%m_%d_%H");
const formatTime = d3.timeFormat("%-H%p %d/%m/%y");
let scrape_date = []

let data = d3.json(urlo)
	.then(response => {

		keep = response.map(d => d)
		keep = keep.filter(d => !remove.includes(d.Page))
		// keys = Object.keys(keep[0])
		// console.log("Keys: ", keys)
		// console.log("Keep: ", keep)
		tableData = keep.map(d => d)


	})

$: scrape_date = formatTime(parseTime([...new Set(keep.map(d => d.scraped_datetime))][0]))
$: console.log("scrape_date: ", scrape_date)
let sortBy = {col: "Rank", ascending: true};

let search = ''

$: sort = (column) => {
		
		if (sortBy.col == column) {
			sortBy.ascending = !sortBy.ascending
		} else {
			sortBy.col = column
			sortBy.ascending = true
		}
		
		// Modifier to sorting function for ascending or descending
		let sortModifier = (sortBy.ascending) ? 1 : -1;
		
		let sort = (a, b) => 
			(a[column] < b[column]) 
			? -1 * sortModifier 
			: (a[column] > b[column]) 
			? 1 * sortModifier 
			: 0;

		// tableData = keep.map(d => d)

		// tableData = tableData.sort(sort);

		keep = keep.sort(sort);




	}


$: tableData = keep.filter(d => d.Page.toLowerCase().includes(search.toLowerCase()))

$: console.log("lengthof: ", tableData.length)

function replacer(stringo){
	// let resulto = stringo.replace('_', ' ')

	let resulto
	if (typeof stringo === 'string'){
		resulto = stringo.replaceAll('_', ' ')
	} else {
		resulto = stringo
	}

	// console.log(stringo)
	// console.log(typeof(stringo))
	// console.log(resulto)
	return resulto

}

</script>

<div class='container w-full'>
	<h1>{title}</h1>
	<p class='subhead'>Last updated {scrape_date}</p>
<input type="search" bind:value={search} placeholder="Search for page" class="mx-auto w-2/3 mb-5 bg-slate-100 text-center">

<div class='overflow-y-scroll h-60'>

	<table class="table-auto w-full">
		<thead class='bg-white border-b sticky top-0'>
			<tr>
				{#each keys as columnHeading}
					<th on:click={sort(columnHeading)}>{columnHeading}</th>
				{/each}
			<tr/>
		</thead>
		<tbody>
			{#each Object.values(tableData) as row}
				<tr class='bg-white border-b'>
					{#each keys as key}
						<td>{replacer(row[key])}</td>
					{/each}
				</tr>
			{/each}
		</tbody>
	</table>
	</div>

</div>
<style>

	.container {margin-top: 50px;
	margin-bottom: 50px;}
	table {
		background-color: #fff;
		text-align: center;
		/* border-collapse: collapse; */
		/* width: 100%; */
		/* height: 100%; */
		/* overflow-y: auto; */
		border-spacing: 0px;
	}
	tr {
		/* border-bottom: 0.2px solid #ccc; */
	}
	th {
		/* border-bottom: 0.5px solid #000; */
		padding-bottom: 5px;
		font-size: 1em;
	}
	thead {
		/* position: sticky; */
		text-align: center;
		background-color: #fff;
		/* position: fixed; */
		/* top: 0; */

		stroke: #000;
	}



	.container h1{
  /* margin-top: 20px; */
  /* margin-bottom: 10px; */
  text-align: center;
  font-size: 2em;
}

.subhead{
		text-align: center;
		text-anchor: middle;
		margin-bottom: 10px;
	}
</style>