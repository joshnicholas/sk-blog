<script>
    import * as d3 from 'd3';
    import { Styles,Input } from 'sveltestrap';
 
  

	export let title
    export let urlo;
    export let keys
    export let removeCol
    export let standfirst

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
  

  
  let keep = []
  let inter
//   let keys = ["Headline","Rank"]
  
let non_rank = keys.map(d => d)
non_rank = non_rank.filter(d => d != "Rank")

  let data = d3.json(urlo)
      .then(response => {
  
        //   keep = response.map(d => d)
          response.forEach(function(value, index, array) {

        value['Search_var'] = Object.values(value).join(" ")
        keep.push(value)
          })

          keep = keep.filter(d => !remove.includes(d[removeCol]))

          tableData = keep.map(d => d)
  
      })
  
const parseTime = d3.timeParse("%Y_%m_%d_%H");
const formatTime = d3.timeFormat("%-I%p %d/%m/%Y");
let scrape_date
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
  
          tableData = keep.map(d => d)
  
          tableData = tableData.sort(sort);
  
        //   keep = keep.sort(sort);

        console.log("Sort")
  
      }
  

    $: tableData = keep.filter(d => d['Search_var'].toLowerCase().includes(search.toLowerCase()))
  
  
  </script>
  
  <div class='container w-full'>
	<h1 class='text-3xl'>{title}</h1>
    <p class='subhead text-xs mb-5'>{standfirst}Last updated ~{scrape_date.replace('AM', 'am').replace('PM', 'pm')}</p>
    <input  class="rounded-md m-auto w-1/3 bg-slate-100 text-left mb-5" type="search" bind:value={search} placeholder="Search">

  <div class='overflow-y-scroll max-h-80'>
      <table class="table-auto w-full">
          <thead class='bg-white border-b sticky top-0 text-left'>
              <tr class='pr-4 p-8 text-left'>
                  {#each non_rank as columnHeading}
                      <th class='bg-white text-left pr-4' on:click={sort(columnHeading)}>{columnHeading}</th>
                  {/each}
                  <th class='bg-white text-right pr-4' on:click={sort("Rank")}>{"Rank"}</th>

              <tr/>
          </thead>
          <tbody>
              {#each Object.values(tableData) as row}
              <tr class='bg-white border-b text-left py-8 px-10'>
                      {#each non_rank as key}
                          <td class='bg-white text-left text-base pr-4'>{row[key]}</td>
                      {/each}
                      <td class='bg-white text-right text-base  pr-4'>{row["Rank"]}</td>
                  </tr>
              {/each}
          </tbody>
      </table>
      </div>
  </div>



  <style>
  
      table {
          background-color: #fff;
      }

.container {margin-top: 50px;
	margin-bottom: 50px;}

  </style>