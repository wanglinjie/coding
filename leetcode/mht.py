package hello;

//import java.util.Scanner;
import java.util.*;
import java.math.*;

public class hello {

    public static void main(String[] args) {
        // TODO Auto-generated method stub
        //int[][] edges = new int[4][4];
        // int[][] edges = {{0, 1, 0, 0}, {1, 0, 1, 1}, {0, 1, 0, 0}, {0, 1, 0, 0}};
        int[][] edges = {{0, 3}, {1, 3}, {2, 3}, {4, 3}, {5, 4}};
        // int[][] edges ={{0,1},{1,2},{1,3},{2,4},{3,5},{4,6}};
        // int[][] edges = {{0,1},{0,2},{0,3},{2,4},{0,5},{5,6},{6,7},{2,8},{7,9}};
        // System.out.println(edges[3][1]);
        //findMinHeightTrees(12, edges);
        List list;
        hello he = new hello();
        long startTime=System.currentTimeMillis();   //获取开始时间
        list = he.findMinHeightTrees(6, edges);
        long endTime=System.currentTimeMillis(); //获取结束时间  
        System.out.println("程序运行时间： "+(endTime-startTime)+"ms"); 
        System.out.println(list);
    }
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        // List last = new ArrayList();
        // int row = edges.length;
        // int col = edges[0].length;
        // int[][] graph = new int[row][col];
        // List<Object[][]> list = new ArrayList<Object[][]>();
        int[][] graph = new int[n][n];
        int point1, point2;
        for(int i = 0; i < edges.length; i++) {
            point1 = edges[i][0];
            point2 = edges[i][1];
            graph[point1][point2] = 1;
            graph[point2][point1] = 1;
        }
        List list = new ArrayList();
        for(int i = 0; i < n; i++) {
            list.add(i);
        }
        System.out.println(list.size());
        List removelist = new ArrayList();
        List conpoint = new ArrayList();
        while (list.size() > 2) {
            //  System.out.println(list.size());
            removelist.clear();
            for(int i = 0; i < list.size(); i++) {
                //System.out.println("list.size() "+list.size()); 
                int point = (int)list.get(i);
                //System.out.println("get " + point);
                // int edgeNum = 0;
                //List conpoint = new ArrayList();
                conpoint.clear();
                for(int j = 0; j < n; j++) {
                    if(graph[point][j] == 1) {
                        conpoint.add(j);
                    }
                }
                if(conpoint.size() < 2) {
                    removelist.add(i);
                    System.out.println("remove " + i);
                }
            }
            for(int i = removelist.size()-1; i >= 0; i--) {
                
                int point = (int)removelist.get(i);
                System.out.print(i);
                System.out.println(" " +point);
                for(int j=0; j < n; j++) {
                    graph[j][(int)list.get(point)] = 0;
                    //graph[(int)conpoint.get(j)][point] = 0;
                }
                //System.out.println(point);
                list.remove(point);
            }
        }
        return list;
    }
    
    public void printhello(String result) {
        System.out.print(result);
    }
}

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        children = collections.defaultdict(set)
        for s, t in edges:
            children[s].add(t)
            children[t].add(s)
        vertices = set(children.keys())
        while len(vertices) > 2:
            leaves = [x for x in children if len(children[x]) == 1]
            for x in leaves:
                for y in children[x]:
                    children[y].remove(x)
                del children[x]
                vertices.remove(x)
        return list(vertices) if n != 1 else [0]