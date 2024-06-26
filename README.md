# Scottish Election Information 

This is a repository containing the data from 1070 Scottish elections
conducted in the years 2007, 2012, 2017, and 2022. This data
was originally put together thanks to the work of David McCune, whose original
1100 BLT files are included in the `blt_files` folder. These 1100 election
files include an additional 30 "by" elections (a.k.a special elections) which
were not translated into CSV files due to a lack of party labels within the
original BLT files.

Scottish council elections are conducted using voting model known as Single
Transferrable Vote (STV) wherein the constituent has the option to rank the 
people that they are voting for. In the event that their top choice is then
eliminated from the race, their vote is then transferred to their next most favored
candidate.


## How to Read a the CSV files

The CSV files compiled here follow a similar format to the BLT files from which they were
derived. Here is a simple synopsis of the data contained in each of the rows of the file:

- **Row 1:** Number of candidates number of seats
- **Rows After Row 1 Containing Ballot Lists:** 
  - The first item of the row is the number of ballots of the type described by the
    remaining numbers in the row
  - All numbers in the row following the first number describe the ordering of the ballot,
    so a row with the description `12,3,1,2` says that there were 12 ballots where
    candidate 3 was most preferred, followed by 1, and lastly followed by 2
- **Rows Following Ballot Lists:** There are two types of rows following the ballots.
  Immediately following the ballots is a list of candidates listed in-order. So the first
  candidate to appear in this list corresponds to candidate 1 on the ballot, the second 
  candidate to appear in the list corresponds to candidate 2 on the ballot, and so on.
  The last line of the file contains the name of the Ward wherein the election was held.

### Example CSV file with Comments

Here is an example BLT file

```
3,2,
12,1,
88,1,3,2,
14,2,3,
8,3,
"Candidate 1","Alvin the First","Party A (A)",
"Candidate 2","Becca the Second","Party B (B)",
"Candidate 3","Carrie the Third","Party C (C)",
"Wardy McWard Town",
```

How to read it:

```
3,2,                                                # There are 3 candidates running for 2 seats
12,1,                                               # 12 Bullet votes for candidate 1 were cast
88,1,3,2,                                           # 88 Ballots preferring 1 to 3 and 3 to 2 were cast
14,2,3,
8,3,
"Candidate 1","Alvin the First","Party A (A)",      # The name of candidate 1 and their party
"Candidate 2","Becca the Second","Party B (B)",
"Candidate 3","Carrie the Third","Party C (C)",
"Wardy McWard Town",                                # The name of the ward
```

## List of Parties in 2007, 2012, 2017, and 2022 Elections

- Alba Party for Independence (API)
- Bordersm(Borders)
- Britannica Party (BP)
- British National Party (BNP)
- Brittish Unionists (BU)
- Christian Peoples Alliance (CPA)
- Communist Party of Britain (Comm)
- Conservative (Con)
- Cumbernauld Independent Councillors Alliance (CICA)
- East Dunbartonshire Independent Alliance (EDIA)
- East Kilbride Alliance (EKA)
- Freedom Alliance (FA)
- Glasgow First (Glasgow First)
- Green (Gr)
- Independence for Scotland Party (ISP)
- Independent (Ind)
- Independent Alliance North Lanarkshire (IANL)
- Labour (Lab)
- Labour and Co-operative Party (LabCo)
- Liberal (Lib)
- Liberal Democrat (LD)
- Libertaian (Libtn)
- Libertarian (Libtn)
- Monster Raving Loony (MVR)
- National Front (NF)
- No Referendum, Maintain Union, Pro-Brexit (NRMUPB)
- No Referendum, Maintain Union, Pro-Brexit (NUMUPB)
- Orkney Manifesto Group (OMG)
- Piarate (Pir)
- Rubbish (Rubbish)
- Scotland Independent Network (ScIN)
- Scottish Christian (SC)
- Scottish Eco-Federalist Party (SEFP)
- Scottish Family Party (SFP)
- Scottish National Party (SNP)
- Scottish Senior Citizens (SSC)
- Scottish Unionist (SU)
- Scottish Unionist (SUP)
- Social Democratic Party (SDP)
- Socialist (Soc)
- Socialist Labor Party (SLP)
- Socialist Labour
- Socialist Labour Party (SLP)
- Solidarity (Sol)
- Sovereignty (Sov)
- The Pensioner's Party (TPP)
- Trade Unionist and Socialist Coalition (TUSC)
- UK Independence Party (UKIP)
- Vanaguard Party championing Leaderdale and Melrose (VPLM)
- Vangard Party Championing Tweeddale (VPCT)
- Vanguard Party championing Kelso (VPCK)
- Volt UK (Volt UK)
- West Dunbartonshire Community (WDuns)
- Women's Equality Party (WEP)