//find initial points area and store in array from flatern surface
float square_width = detail(0, 'square_width');
int k = chi('k');
float max_r = (k+1.1)*square_width + 0.000001;
i[] @ pt_mask = nearpoints(0, @ P, max_r);



vector pos, other_pos, dir, dirs[];
float dist, dists[];
foreach(int pt; i[] @ pt_mask)
{
    pos = point(0, 'P', @ptnum);
    other_pos = point(0, 'P', pt);
    dir = rint(normalize(other_pos - pos)*1000000)/1000000;
    dist = distance(other_pos, pos);
    append(dirs, dir);
    append(dists, dist);
}
//v[]@dirs = dirs;
//f[]@dists = dists;


int pts[], npts;
pts = i[] @ pt_mask;
npts = len(i[] @ pt_mask);
for(int i=npts-1; i>-1; --i)
{
    for(int j=i-1; j>-1; --j)
    {
        if(length2(dirs[i] - dirs[j])*1000000 <=100 && dists[i] > dists[j])
        {
            removeindex(pts, i);
            break;
        }
    }
}

i[] @ pt_mask = pts;
removevalue(i[] @ pt_mask, @ ptnum);