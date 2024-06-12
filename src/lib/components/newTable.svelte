<script>
    import * as d3 from 'd3';
    import Table from './table.svelte'
    // import { Styles,Input } from 'sveltestrap';
 
  

	export let title
    export let keys
    export let removeCol
    export let standfirst
    export let thingo
    export let datah

    // console.log("data: ", typeof datah)

    // console.log("thingo: ", thingo)


    let remove = ['Portal:Current_events', 'Wikipedia', 'Main_Page', 
'Special:Search', 'Special:Random', "Special:Watchlist",'Special:Randompage',
'Special:Book','Special:CreateAccount','Special:RecentChanges','Help:Your first article',
'Portal:Contents','Wikipedia:Contact us','Wikipedia:About','Wikipedia:Contact_us','Wikipedia:Citation_needed',
'Wikipedia:Featured_pictures']


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
  
    tableData = [...datah]

    // console.log("TableData: ", tableData)

  
  let keep = []
  keep = [...datah]
  let inter
//   let keys = ["Headline","Rank"]
  
let non_rank = keys.map(d => d)
non_rank = non_rank.filter(d => d != "Rank")


const parseTime = d3.timeParse("%Y_%m_%d_%H");
const formatTime = d3.timeFormat("%-I:17%p %d/%m");
let scrape_date
$: scrape_date = formatTime(parseTime([...new Set(keep.map(d => d.scraped_datetime))][0]))

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
  
          tableData = keep.map(d => d)
  
          tableData = tableData.sort(sort);
  
        //   keep = keep.sort(sort);

        // console.log("Sort")
  
      }
  

    $: tableData = keep.filter(d => d['Search_var'].toLowerCase().includes(search.toLowerCase()))
  
  
// console.log("Object.values(tableData): ", Object.values(tableData))
  </script>

 

  <div class='container w-full'>
	<h1 class='text-3xl'>{title}</h1>
    <p class='subhead text-xs mb-5'>{standfirst}</p>
    <p class='subhead text-xs mb-5'>Last updated ~{scrape_date.replace('AM', 'am').replace('PM', 'pm')} Brisbane Time</p>
    <input  class="bg-neutral-600 rounded-md m-auto w-1/2 text-left mb-5" type="search" bind:value={search} placeholder="Search">

  <div class='overflow-y-scroll max-h-80'>
      <table class="table-auto w-full">
          <thead class='border-b bg-neutral-700 sticky top-0 text-left'>
              <tr class='pr-4 p-8 text-left'>
                  {#each non_rank as columnHeading}
                      <th class='text-left pr-4' on:click={sort(columnHeading)}>{columnHeading}</th>
                  {/each}
                  <th class=' text-right pr-4' on:click={sort("Rank")}>{"Rank"}</th>

              <tr/>
          </thead>
          <tbody>
              {#each Object.values(tableData) as row}
              <tr class='odd:bg-neutral-600 even:bg-neutral-500 border-b text-left py-8 px-10'>
                      {#each non_rank as key}
                        {#if thingo == "Wiki"}
                        <td class='text-left pr-4'>{row[key]} - <strong style="color: #FF5733;"><a href="https://en.wikipedia.org/wiki/{row['Page']}" target="_blank">Link</a></strong></td>
                        {:else if thingo != "goog_trends"}
                        <td class=' text-left pr-4'>{row[key]} - <strong style="color: #FF5733;"><a href={row['Url']} target="_blank">Link</a></strong></td>
                        {:else}
                          <td class=' text-left pr-4'>{row[key]}</td>
                          {/if}                      
                        {/each}
                      <td class=' text-right  pr-4'>{row["Rank"]}</td>
                  </tr>
              {/each}
          </tbody>
      </table>
      </div>
  </div>



  <style>
  
      /* table {
          background-color: #fff;
      } */

.container {margin-top: 50px;
	margin-bottom: 20px;
  padding-left: 10px;
  padding-right: 10px;
  }


  @media only screen and (max-width: 600px) {
    .container {margin-top: 50px;
	margin-bottom: 10px;
  padding-left: 0px;
  padding-right: 0px;}
}


  </style>