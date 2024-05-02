/** 
* 点集 单向Hausdorff 距离算法
* @param {array} a - 点集列表
* @param {array} b - 点集列表
* @return {number} - Hausdorff（a,b）
* 即：对于a点集中的每一点找寻其到b点集中的最小距离 然后在这些距离中取最大值
*/
function getunidirectionalHausdorffDistance(a,b){
    let a1=a;
    let b1=b;
    let a_b=[];
    let mindic=[];
    for( let i=0;i<a1.length;i++){
        let p0=a1[i];
        for (let j=0;j<b1.length;j++){
            let p1=b1[j];
            a_b.push(p0.getEuclideanDistance_(p1));
        }
        mindic.push(Math.min(...a_b)) //对于a点集中的每一点找寻其到b点集中的最小距离
        a_b=[];
    }
    return Math.max(...mindic); // 然后在这些距离中取最大值
}

/** 
* 点集 双向Hausdorff 距离算法
* @param {array} a - 点集列表
* @param {array} b - 点集列表
* @return {number} - bidirectionalHausdorff（a,b）
* 即：max(Hausdorff（a,b）,Hausdorff（b,a）)
*/
function getbidirectionalHausdorffDistance(a,b){
    return Math.max(
        getunidirectionalHausdorffDistance(a,b),
        getunidirectionalHausdorffDistance(b,a)
    )
}