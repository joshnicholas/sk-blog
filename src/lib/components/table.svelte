<script>
    export let datah
    export let keys
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
            {#each Object.values(datah) as row}
                <tr>
                    {#each Object.values(row) as cell}
                        <td>{cell}</td>
                    {/each}
                </tr>
            {/each}
        </tbody>
    </table>
    </div>