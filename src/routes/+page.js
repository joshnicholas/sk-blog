/** @type {import('./$types').PageLoad} */

export const load = async ({ fetch }) => {
    const latestRes = await fetch(`https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/feed/latest.json`);
    const latest = await latestRes.json()

    return { latest: latest };
}




// export async function load({ fetch }) 
// {	const res = await fetch(`https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/feed/latest.json`);	
// const item = await res.json();
// return { item };}



