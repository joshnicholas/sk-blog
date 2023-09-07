<script>
    import * as d3 from 'd3';
    import { Styles,Input } from 'sveltestrap';
    import Table from '$lib/components/table.svelte'
  
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
  

  
  let keep = []
  let inter
  let keys = ["Rank", "Headline"]
  
  let data = d3.json(urlo)
      .then(response => {
  
          keep = response.map(d => d)
        //   keys = Object.keys(keep[0])
          // console.log("Keep: ", keep)
          tableData = keep.map(d => d)
  
      })
  
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
  

  
  
  </script>
  

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
                  <tr>
                      {#each keys as key}
                          <td>{row[key]}</td>
                      {/each}
                  </tr>
              {/each}
          </tbody>
      </table>
      </div>
  
  <style>
  
      table {
          background-color: #fff;
          text-align: center;
          /* border-collapse: collapse; */
          /* width: 100%; */
          /* height: 100%; */
          /* overflow-y: auto; */
          border-spacing: 0px;
      }
      th {
          /* border-bottom: 0.5px solid #000; */
          padding-bottom: 5px;
          font-size: 1.1em;
      }
      thead {
          /* position: sticky; */
          text-align: center;
          background-color: #fff;
          /* position: fixed; */
          /* top: 0; */
  
          stroke: #000;
      }
  
  
  
  </style>